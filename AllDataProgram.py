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

file = uproot.open("ttbar.root")
events = uproot.open("ttbar.root")["events"]

##--Constants--##
Length = len(Jet_E)
tM = np.linspace(1.75, 5.75, num=200)
zM=np.linspace(5, 55, num=100)
yM =np.linspace(0,1500, num=250)

##--DATA--#####################################################################

## Jet Data
NJet = events.array("NJet")
Jet_Px, Jet_Py, Jet_Pz = events.arrays("Jet_P[xyz]*", outputtype = collections.namedtuple)
Jet_E = events.array("Jet_E")
Jet_btag = events.array("Jet_btag")
Jet_ID = events.array("Jet_ID")

## Muon Data
NMuon = events.array("NMuon")
Muon_Px, Muon_Py, Muon_Pz = events.arrays("Muon_P[xyz]*", outputtype = collections.namedtuple)
Muon_E = events.array("Muon_E")
Muon_Charge = events.array("Muon_Charge")
Muon_Iso = events.array("Jet_ID")

## Electron Data
NElectron = events.array("NElectron")
Electron_Px, Electron_Py, Electron_Pz = events.arrays("Electron_P[xyz]*", outputtype = collections.namedtuple)
Electron_E = events.array("Electron_E")
Electron_Charge = events.array("Electron_Charge")
Electron_Iso = events.array("Electron_Iso")

## Photon Data
NPhoton = events.array("NPhoton")
Photon_Px, Photon_Py, Photon_Pz = events.arrays("Photon_P[xyz]*", outputtype = collections.namedtuple)
Photon_E = events.array("Photon_E")
Photon_Iso = events.array("Photon_Iso")

## MET Data
MET_Px, MET_Py = events.arrays("MET_p[xy]*", outputtype = collections.namedtuple)

## M Data
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

#
# Analyze 
#

## Finding Esys 
Esys = [] 
for x in range(0, Length): 
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
    
## Finding Psys
Psys = [] 
PsysX = []
PsysY = []
PsysZ = []
for x in range(0, Length): 
    newPsysX = 0
    newPsysY = 0
    newPsysZ = 0
    if not Jet_Px[x].size == 0 :
        newPsysX += Jet_Px[x][0]
    if not Jet_Py[x].size == 0 :
        newPsysY += Jet_Py[x][0]
    if not Jet_Pz[x].size == 0 :
        newPsysZ += Jet_Pz[x][0]
        
    if not Muon_Px[x].size == 0 :
        newPsysX += Muon_Px[x][0]
    if not Muon_Py[x].size == 0 :
        newPsysY += Muon_Py[x][0]
    if not Muon_Pz[x].size == 0 :
        newPsysZ += Muon_Pz[x][0]
        
    if not Electron_Px[x].size == 0 :
        newPsysX += Electron_Px[x][0]
    if not Electron_Py[x].size == 0 :
        newPsysY += Electron_Py[x][0]
    if not Electron_Pz[x].size == 0 :
        newPsysZ += Electron_Pz[x][0]
        
    if not Photon_Px[x].size == 0 :
        newPsysX += Photon_Px[x][0]
    if not Photon_Py[x].size == 0 :
        newPsysY += Photon_Py[x][0]
    if not Photon_Pz[x].size == 0 :
        newPsysZ += Photon_Pz[x][0]
      
    PsysX.append(newPsysX) 
    PsysY.append(newPsysY) 
    PsysZ.append(newPsysZ) 
    newPsys = newPsysX**2 + newPsysY**2 + newPsysZ**2
    Psys.append(newPsys)
<<<<<<< Updated upstream
=======

## Velocity Stuff 
B = []
for x in range(0, Length):
    newPx=PsysX[x]
    newPy=PsysY[x]
    newPz=PsysZ[x]
    newEsys=Esys[x]
    if newEsys[0]!=0:
        Bx=newPx/newEsys
        By=newPy/newEsys
        Bz=newPz/newEsys
        # Calculate Bsys, B and Gam for the current event
        #B=momentum/energy
        Bsq=Bx**2+By**2+Bz**2
        sqrtB=math.sqrt(Bsq)
        B.append(sqrtB)
    
    
## Finding Invariant Mass
InvMass = []
for x in range(0, Length):
    if (Esys[x][0]**2 - Psys[x] > 0):
        if (Esys[x][0] != 0):
            newInvMass = math.sqrt((Esys[x][0]**2) - Psys[x])
        else: 
            newInvMass = 0
    else:
        newInvMass = 0
    InvMass.append(newInvMass)


## Histograms
plt.subplot(1, 3, 1)
plt.hist(Esys, zM)
plt.title('Energy of the System')

plt.subplot(1, 3, 2)
plt.hist(Psys, yM)
plt.title('Momentum of the System')

plt.subplot(2, 2, 1)
plt.hist(InvMass, tM)
plt.title('Invariant Mass')
>>>>>>> Stashed changes
