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

file = uproot.open("data.root")
events = uproot.open("data.root")["events"]

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
Muon_Iso = events.array("Muon_Iso")

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
MET_Px, MET_Py = events.arrays("MET_p[xy]*", outputtype = collections.namedtuple)

#M Data
MChadronicBottom_Px, MChadronicBottom_Py, MChadronicBottom_Pz = events.arrays("MChadronicBottom_p[xyz]*", outputtype = collections.namedtuple)
MCleptonicBottom_Px, MCleptonicBottom_Py, MCleptonicBottom_Pz = events.arrays("MCleptonicBottom_p[xyz]*", outputtype = collections.namedtuple)
MChadronicWDecayQuark_Px, MChadronicWDecayQuark_Py, MChadronicWDecayQuark_Pz = events.arrays("MChadronicWDecayQuark_p[xyz]*", outputtype = collections.namedtuple)
MChadronicWDecayQuarkBar_Px, MChadronicWDecayQuarkBar_Py, MChadronicWDecayQuarkBar_Pz = events.arrays("MChadronicWDecayQuarkBar_p[xyz]*", outputtype = collections.namedtuple)
MClepton_Px, MClepton_Py, MClepton_Pz = events.arrays("MClepton_p[xyz]*", outputtype = collections.namedtuple)
MCleptonPDGid = events.array("MCleptonPDGid")
MCneutrino_Px, MCneutrino_Py, MCneutrino_Pz = events.arrays("MCneutrino_p[xyz]*", outputtype = collections.namedtuple)
NPrimaryVertices = events.array("NPrimaryVertices")
triggerIsoMu24 = events.array("triggerIsoMu24")
EventWeight = events.array("EventWeight")

###############################################################################
Length = len(Jet_E)
            
## Histogram of Muon Multiplicity
plt.figure(1)
plt.hist(NMuon)
plt.xlabel("Muon Multiplicity")

## Calculating Esys for Two Muons of Opposite Charge
MuonEsys = [] 
for x in range(0, Length): 
    if NMuon[x] == 2:
        if Muon_Charge[x][0] != Muon_Charge[x][1]:
            newMuonEsys = Muon_E[x][0] + Muon_E[x][1]
            MuonEsys.append(newMuonEsys) #Appends Array
            
## Calculating Psys for Two Muons of Opposite Charge
MuonPsys = [] 
MuonPsysX = []
MuonPsysY = []
MuonPsysZ = []
for x in range(0, Length): 
    if NMuon[x] == 2:
        if Muon_Charge[x][0] != Muon_Charge[x][1]:
            newMuonPsysX = Muon_Px[x][0] + Muon_Px[x][1]
            newMuonPsysY = Muon_Py[x][0] + Muon_Py[x][1]
            newMuonPsysZ = Muon_Pz[x][0] + Muon_Pz[x][1]
            MuonPsysX.append(newMuonPsysX) 
            MuonPsysY.append(newMuonPsysY) 
            MuonPsysZ.append(newMuonPsysZ) 
            newMuonPsys = newMuonPsysX**2 + newMuonPsysY**2 + newMuonPsysZ**2
            MuonPsys.append(newMuonPsys)

## Calculating Invariant Mass for Two Muons of Opposite Charge
MuonInvMass = []
for x in range(0, len(MuonEsys)):
    newMuonInvMass = math.sqrt((MuonEsys[x]**2) - MuonPsys[x])
    MuonInvMass.append(newMuonInvMass)
    
## Histogram of the Invariant Mass of Two Muons of Opposite Charge
plt.figure(2)
aM = np.linspace(0, 500, num = 250)
plt.hist(MuonInvMass, aM)
plt.xlabel("Mass of Two Muons of Opposite Charge")
plt.yscale("log")

plt.figure(3)
bM = np.linspace(0, 5, num = 200)
plt.hist(MuonInvMass, bM)
plt.xlabel("Mass of Two Muons of Opposite Charge")

plt.figure(4)
cM = np.linspace(5, 12, num = 200)
plt.hist(MuonInvMass, cM)
plt.xlabel("Mass of Two Muons of Opposite Charge")


plt.figure(5)
dM = np.linspace(12, 120, num = 300)
plt.hist(MuonInvMass, dM)
plt.xlabel("Mass of Two Muons of Opposite Charge")
