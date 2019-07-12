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

import ROOT
ROOT.gROOT.ProcessLine(".x tdrstyle.C")

# Was Originally
#from OutreachExercise2011.DecaysToLeptons.sources import sources
# Changed to
from QuarkNet-CMS-Data-Summer-2019.FromOutreach.sources import sources

# Import the Analyzer you want to run:
# FourLeptonAnalyzer or TwoLeptonAnalyzer
# by uncommenting the appropiate line below. 

# Was Originally
#from OutreachExercise2011.DecaysToLeptons.FourLeptonAnalyzer import FourLeptonAnalyzer as MyAnalyzer
#from OutreachExercise2011.DecaysToLeptons.TwoLeptonAnalyzer import TwoLeptonAnalyzer as MyAnalyzer

# Changed To
from QuarkNet-CMS-Data-Summer-2019.FromOutreach.TwoLeptonAnalyzer import TwoLeptonAnalyzer as MyAnalyzer

analyzer = MyAnalyzer()

analyzer.declareHistos()

for sample in sources:
    # maxEv defines the maximum number of events to analyze
    # set it to -1 to analyze all available events; 
    analyzer.processSample(sample, maxEv=-1)


analyzer.makeAllPlots()

# uncommet line below to export selected data to a json file
#analyzer.exportData()


