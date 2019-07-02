# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 09:49:17 2019

@author: QuarkNet
"""

import uproot
import numpy as np
import matplotlib.pyplot as plt
import math
import collections

nP = 100000

file = uproot.open("HEPTutorial/files/data.root")
events = uproot.open("HEPTutorial/files/data.root")["events"]

##--DATA--#####################################################################

#Jet Data
NJet = events.array("NJet")
#Jet_P = events.arrays("Jet_P[xyz]*")
Jet_Px, Jet_Py, Jet_Pz = events.arrays("Jet_P[xyz]*", outputtype = collections.namedtuple)
Jet_E = events.array("Jet_E")
Jet_btag = events.array("Jet_btag")
Jet_ID = events.array("Jet_ID")

#Muon Data
NMuon = events.array("NMuon")
#Muon_P = events.arrays("Muon_P[xyz]*", outputtype = collections.namedtuple)
Muon_Px, Muon_Py, Muon_Pz = events.arrays("Muon_P[xyz]*", outputtype = collections.namedtuple)
Muon_E = events.array("Muon_E")
Muon_Charge = events.array("Muon_Charge")
Muon_Iso = events.array("Jet_ID")

#Electron Data
NElectron = events.array("NElectron")
#Electron_P = events.arrays("Electron_P[xyz]*", outputtype = collections.namedtuple)
Electron_Px, Electron_Py, Electron_Pz = events.arrays("Electron_P[xyz]*", outputtype = collections.namedtuple)
Electron_E = events.array("Electron_E")
Electron_Charge = events.array("Electron_Charge")
Electron_Iso = events.array("Electron_Iso")

#Photon Data
NPhoton = events.array("NPhoton")
#Photon_P = events.arrays("Photon_P[xyz]*", outputtype = collections.namedtuple)
Photon_Px, Photon_Py, Photon_Pz = events.arrays("Photon_P[xyz]*", outputtype = collections.namedtuple)
Photon_E = events.array("Photon_E")
Photon_Iso = events.array("Photon_Iso")

#MET Data
MET_P = events.arrays("MET_p[xy]*", outputtype = collections.namedtuple)

#M Data
MChadronicBottom_P = events.arrays("MChadronicBottom_p[xyz]*", outputtype = collections.namedtuple)
MCleptonicBottom_p = events.arrays("MCleptonicBottom_p[xyz]*", outputtype = collections.namedtuple)
MChadronicWDecayQuark_P = events.arrays("MChadronicWDecayQuark_p[xyz]*", outputtype = collections.namedtuple)
MChardronicWDecayQuarkBar_P = events.arrays("MChardronicWDecayQuarkBar_p[xyz]*", outputtype = collections.namedtuple)
MClepton_P = events.arrays("MClepton_p[xyz]*", outputtype = collections.namedtuple)
MCleptonPDGid = events.array("MCleptonPDGid")
MCneutrino_P = events.arrays("MCneutrino_p[xyz]*", outputtype = collections.namedtuple)
NPrimaryVertices = events.array("NPrimaryVertices")
triggerIsoMu24 = events.array("triggerIsoMu24")
EventWeight = events.array("EventWeight")

###############################################################################


#
# Analyze 
#

## Finding Esys 
Esys = [] 
for x in range(0, len(Jet_E)): 
    newEsys = [0]
    if not Jet_E[x].size == 0 :
        newEsys += Jet_E[x][0]
    if not Muon_E[x].size == 0 :
        newEsys += Muon_E[x][0]
    if not Electron_E[x].size == 0 :
        newEsys += Electron_E[x][0]
    if not Photon_E[x].size == 0 :
        newEsys += Photon_E[x][0]
    Esys.append(newEsys) #Appends Array
    
#Finding Psys
Psys = [] 
for x in range(0, len(Jet_Px)): 
    newPsys = [0]
    if not Jet_Px[x].size == 0 :
        newPsys += Jet_Px[x][0]
    if not Jet_Py[x].size == 0 :
        newPsys += Jet_Py[x][0]
    if not Jet_Pz[x].size == 0 :
        newPsys += Jet_Pz[x][0]
        
    if not Muon_Px[x].size == 0 :
        newPsys += Muon_Px[x][0]
    if not Muon_Py[x].size == 0 :
        newPsys += Muon_Py[x][0]
    if not Muon_Pz[x].size == 0 :
        newPsys += Muon_Pz[x][0]
        
    if not Electron_Px[x].size == 0 :
        newPsys += Electron_Px[x][0]
    if not Electron_Py[x].size == 0 :
        newPsys += Electron_Py[x][0]
    if not Electron_Pz[x].size == 0 :
        newPsys += Electron_Pz[x][0]
        
    if not Photon_Px[x].size == 0 :
        newPsys += Photon_Px[x][0]
    if not Photon_Py[x].size == 0 :
        newPsys += Photon_Py[x][0]
    if not Photon_Pz[x].size == 0 :
        newPsys += Photon_Pz[x][0]
        
    Psys.append(newPsys) #Appends Array  
        
#edit
