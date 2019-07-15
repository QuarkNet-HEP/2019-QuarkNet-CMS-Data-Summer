## This file is part of CMSOutreachExercise2011 derived from CMSOutreachExercise2010.
## Copyright (C) 2014 Instituto de Fisica de Cantabria and CERN.
## Based on the code of the CMSData Analysis School 2014 Long Exercise: 
## Search for the Higgs in ZZ -> 4 leptons decay channel (available 
## at https://github.com/bachtis/CMSDAS)

## CMSOutreachExercise2011 is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## CMSOutreachExercise2011 is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with CMSOutreachExercise2011. If not, see <http://www.gnu.org/licenses/>.

from DataFormats.FWLite import Events, Handle
# Was Originally
#from OutreachExercise2011.DecaysToLeptons import rootnotes
# Changed to
from QuarkNet-CMS-Data-Summer-2019.FromOutreach import rootnotes

import ROOT
import os
import json
import time

# Was Originaly
#def getFullPath(path):
#    return os.path.join(os.environ['CMSSW_BASE'],
#                        'src/OutreachExercise2011/DecaysToLeptons',
#                        path)

# Changed to
def getFullPath(path):
    return os.path.join(os.environ['CMSSW_BASE'],
                        'src/QuarkNet-CMS-Data-Summer-2019/FromOutreach',
                        path)





class EventBox(object):
    def __init__(self):
        self.Z1_l1 = None
        self.Z1_l2 = None
        self.Z2_l1 = None
        self.Z2_l2 = None


class Object(object):
    """
    What is this?
    """
    def __init__(self, l1, l2=None):
        self.l1 = l1
        self.l2 = l2
        if l2:
            self.p4 = ROOT.TLorentzVector(self.l1.px() + self.l2.px(),
                                          self.l1.py() + self.l2.py(),
                                          self.l1.pz() + self.l2.pz(),
                                          self.l1.energy() + self.l2.energy())
        else:
            self.p4 = ROOT.TLorentzVector(self.l1.px(),
                                          self.l1.py(),
                                          self.l1.pz(),
                                          self.l1.energy())

    def mass(self):
        return self.p4.M()

    def pdgId(self):
        return 23

    def p4(self):
        return self.p4

    def pt(self):
        return self.p4.Pt()

    def px(self):
        return self.p4.Px()

    def py(self):
        return self.p4.Py()

    def pz(self):
        return self.p4.Pz()

    def energy(self):
        return self.p4.Energy()


class Analyzer (object):
    """
    Skeleton for building Analyzers
    """

    def __init__(self):
        self.vertexHandle = Handle('std::vector<reco::Vertex>')
        self.muonHandle = Handle('std::vector<pat::Muon>')
        self.electronHandle = Handle('std::vector<pat::Electron>')
        self.histograms = {}
        self.samples = ['data']
        self.plots = {}
        for sample in self.samples:
            self.histograms[sample] = {}
        self.data = []

    def muonID(self, muon, vertex):
        """
        Subclasses of Analyzer should define this method
        """
        return True

    def electronID(self, electron, vertex):
        """
        Subclasses of Analyzer should define this method
        """
        return True

    def leptonID(self, lepton, vertex):
        try:
            if abs(lepton.pdgId()) == 11:
                return self.electronID(lepton, vertex)
            elif abs(lepton.pdgId()) == 13:
                return self.muonID(lepton, vertex)
        except ZeroDivisionError:
            return False

    def readCollections(self, event, box, isFake=False):
        event.getByLabel('offlinePrimaryVertices', self.vertexHandle)
        event.getByLabel('patMuons', self.muonHandle)
        event.getByLabel('patElectrons', self.electronHandle)

        box.muons = self.muonHandle.product()
        box.electrons = self.electronHandle.product()
        box.vertex = self.vertexHandle.product()[0]

        #first select muons and electrons
        box.selectedMuons = []
        for mu in box.muons:
            if mu.pt() < 5 or abs(mu.eta()) > 2.4:
                continue
            try:
                if self.muonID(mu, box.vertex):
                    box.selectedMuons.append(mu)
            except ZeroDivisionError:
                continue

        box.selectedElectrons = []
        for ele in box.electrons:
            if ele.pt() < 5 or abs(ele.eta()) > 2.5:
                continue
            try:
                if self.electronID(ele, box.vertex):
                    box.selectedElectrons.append(ele)
            except ZeroDivisionError:
                continue

    def exportData(self):
        f = open('data.json', 'w')
        info = {'data': self.data}
        json.dump(info, f)
        f.close()

    def analyze(self, box):
        return True

    def declareHistos(self):
        return True

    def fillHistos(self, box, sample, weight=1):
        return True

    def declareHisto(self, name, bins, min, max, xlabel=''):
        for sample in self.samples:
            self.histograms[sample][name] = ROOT.TH1F(sample + '_' + name,
                                                      name, bins, min, max)
            self.histograms[sample][name].GetXaxis().SetTitle(xlabel)
            self.histograms[sample][name].GetYaxis().SetTitle('events')

    def fillHisto(self, name, sample, value, weight=1):
        self.histograms[sample][name].Fill(value, weight)

    def addEvent(self, box):
        return

    def processSample(self, sample, maxEv=-1):
        print 'Processing Files'
        print sample.files

        events = Events(sample.files)
        print "%s events available for processing" % events.size()
        ts = time.time() 
        for N, event in enumerate(events):
            if maxEv >= 0 and (N + 1) >= maxEv:
               break
            if N % 1000000 == 0:
                t2 = time.time()
                print "%s events processed in %s seconds" % (N + 1, t2 - ts)
            weight = 1
            box = EventBox()
            self.readCollections(event, box)
            if not self.analyze(box):
                continue
            self.addEvent(box)
            self.fillHistos(box, sample.type, weight)
        tf = time.time()
        print "%s events processed in %s seconds" % (N + 1, tf - ts)

    def convertToPoisson(self, h):
        graph = ROOT.TGraphAsymmErrors()
        q = (1 - 0.6827) / 2.

        for i in range(1, h.GetNbinsX() + 1):
            x = h.GetXaxis().GetBinCenter(i)
            # XXX NOT USED!
            # xLow = h.GetXaxis().GetBinLowEdge(i)
            # xHigh = h.GetXaxis().GetBinUpEdge(i)
            y = h.GetBinContent(i)
            yLow = 0
            yHigh = 0
            if y != 0.0:
                yLow = y - ROOT.Math.chisquared_quantile_c(1 - q, 2 * y) / 2.
                yHigh = ROOT.Math.chisquared_quantile_c(q,
                                                        2 * (y + 1)) / 2. - y
                graph.SetPoint(i - 1, x, y)
                graph.SetPointEYlow(i - 1, yLow)
                graph.SetPointEYhigh(i - 1, yHigh)
                graph.SetPointEXlow(i - 1, 0.0)
                graph.SetPointEXhigh(i - 1, 0.0)

        graph.SetMarkerStyle(20)
        graph.SetLineWidth(2)
        graph.SetMarkerSize(1.)
        graph.SetMarkerColor(ROOT.kBlack)

        return graph

    def makePlot(self, histogram):
        # XXX NOT USED!
        # sandbox = []
        #canvas = ROOT.TCanvas(histogram)
        #if histogram in self.plots:
        #    return self.plots[histogram]['canvas']
        canvas = rootnotes.canvas(histogram)
        canvas.cd()
        ROOT.gStyle.SetOptStat(0)
        ROOT.gStyle.SetOptTitle(0)
        canvas.Range(-68.75, -7.5, 856.25, 42.5)
        canvas.SetFillColor(0)
        canvas.SetBorderMode(0)
        canvas.SetBorderSize(2)
        canvas.SetTickx(1)
        canvas.SetTicky(1)
        canvas.SetLeftMargin(0.15)
        canvas.SetRightMargin(0.05)
        canvas.SetTopMargin(0.05)
        canvas.SetBottomMargin(0.15)
        canvas.SetFrameFillStyle(0)
        canvas.SetFrameBorderMode(0)
        canvas.SetFrameFillStyle(0)
        canvas.SetFrameBorderMode(0)
        canvas.cd()

        frame = canvas.DrawFrame(
            self.histograms['data'][histogram].GetXaxis().GetXmin(),
            0.0, self.histograms['data'][histogram].GetXaxis().GetXmax(), 
            self.histograms['data'][histogram].GetMaximum()*1.2)

        frame.GetXaxis().SetLabelFont(42)
        frame.GetXaxis().SetLabelOffset(0.007)
        frame.GetXaxis().SetLabelSize(0.045)
        frame.GetXaxis().SetTitleSize(0.05)
        frame.GetXaxis().SetTitleOffset(1.15)
        frame.GetXaxis().SetTitleFont(42)
        frame.GetYaxis().SetLabelFont(42)
        frame.GetYaxis().SetLabelOffset(0.007)
        frame.GetYaxis().SetLabelSize(0.045)
        frame.GetYaxis().SetTitleSize(0.05)
        frame.GetYaxis().SetTitleOffset(1.4)
        frame.GetYaxis().SetTitleFont(42)
        frame.GetZaxis().SetLabelFont(42)
        frame.GetZaxis().SetLabelOffset(0.007)
        frame.GetZaxis().SetLabelSize(0.045)
        frame.GetZaxis().SetTitleSize(0.05)
        frame.GetZaxis().SetTitleFont(42)

        frame.GetXaxis().SetTitle(self.histograms['data'][histogram].GetXaxis().GetTitle())
        frame.GetYaxis().SetTitle(self.histograms['data'][histogram].GetYaxis().GetTitle())
        frame.Draw()

        self.histograms['data'][histogram].SetMarkerStyle(20)
        self.histograms['data'][histogram].Sumw2()
        dataG = None
        if self.histograms['data'][histogram].Integral() > 0:
            dataG = self.convertToPoisson(self.histograms['data'][histogram])
            dataG.Draw("Psame")

        legend = ROOT.TLegend(0.74, 0.84, 0.94, 0.94, "", "brNDC")
        legend.SetBorderSize(0)
        legend.SetLineColor(1)
        legend.SetLineStyle(1)
        legend.SetLineWidth(1)
        legend.SetFillColor(0)
        legend.SetFillStyle(0)
        legend.SetTextFont(42)
        legend.AddEntry(self.histograms['data'][histogram], "Data", "p")
        legend.Draw()

        pt = ROOT.TPaveText(0.1577181, 0.9562937, 0.9580537,
                            0.9947552, "brNDC")
        pt.SetBorderSize(0)
        pt.SetTextAlign(12)
        pt.SetFillStyle(0)
        pt.SetTextFont(42)
        pt.SetTextSize(0.03)
        pt.AddText(0.01, 0.4, "CMS")
        pt.Draw()

        self.plots[histogram] = {
            'canvas': canvas,
            'legend': legend,
            'dataG': dataG,
            'latex1': pt}

        canvas.RedrawAxis()
        canvas.Update()

        canvas.SaveAs(histogram+".png")          
       
        return canvas

    def makeAllPlots(self):
        return [self.makePlot(h) for h in self.histograms['data']]
