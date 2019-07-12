#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:25:44 2019

@author: QuarkNet
"""

#DiMuon2019.m
#
# This program is being created to analyze CMS dimuon events
#

## READ THE EVENTS

#
# Read event number, muon quality and 4-momenta data from
# the Comma Separated Value (.csv) file
#

import csv
import numpy as np
import matplotlib.pyplot as plt
import math

nP=99999


data_path = '100k.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data)
    data1 = data[:, 1:]
    data2 = data[:, 0]
    data1=np.array(data1).astype(float)
    

data1 =  np.delete(data1, 69411, axis=0)
data2 =  np.delete(data2, 69411, axis=0)

Run = data1[:, 0]
EvtNum = data1[:, 1]

E1 = data1[:, 2]
px1 = data1[:, 3]
py1 = data1[:, 4]
pz1 = data1[:, 5]
pt1 = data1[:, 6]
eta1 = data1[:, 7]
phi1 = data1[:, 8]

E2 = data1[:, 10]
px2 = data1[:, 11]
py2 = data1[:, 12]
pz2 = data1[:, 13]
pt2 = data1[:, 14]
eta2 = data1[:, 15]
phi2 = data1[:, 16]

Charge1 = data1[:, 9]
Charge2 = data1[:, 17]
Type = data2

MuQuality = []
for x in range(0, nP):
    if Charge1[x] == Charge2[x]:
        newMuQuality = 0
    elif Type[x] == 'GT':
        newMuQuality = 2
    else:
        newMuQuality = 3
    MuQuality.append(newMuQuality)
            
## DIAGNOSTICS

#
# Diagnostic Plots: Histogram all 10 input variables
# in one Figure using subplots
#

plt.figure(1)

plt.subplot(3, 4, 2)
plt.hist(EvtNum)
plt.xlabel('Event Number')

plt.subplot(3, 4, 3)
plt.hist(MuQuality)
plt.xlabel('Muon Quality')

plt.subplot(3, 4, 5)
cM=np.linspace(0, 45, num=200)
plt.hist(E1, cM)
plt.xlabel('Particle 1 Energy (GeV)')

plt.subplot(3, 4, 6)
dM=np.linspace(-10, 10, num=200)
plt.hist(px1, dM)
plt.xlabel('P1 X Momentum (GeV/c)')

plt.subplot(3, 4, 7)
eM=np.linspace(-16, 12.5, num=200)
plt.hist(py1, eM)
plt.xlabel('P1 Y Momentum (Gev/c)')

plt.subplot(3, 4, 8)
fM=np.linspace(-55, 50, num=200)
plt.hist(pz1, fM)
plt.xlabel('P1 Z Momentum (GeV/c)')

plt.subplot(3, 4, 9)
gM=np.linspace(0, 30, num=200)
plt.hist(E2, gM)
plt.xlabel('Particle 2 Energy (GeV)')

plt.subplot(3, 4, 10)
hM=np.linspace(-10, 10, num=200)
plt.hist(px2, hM)
plt.xlabel('P2 X Momentum (GeV/c)')

plt.subplot(3, 4, 11)
plt.hist(py2, hM)
plt.xlabel('P2 Y Momentum (GeV/c)')

plt.subplot(3, 4, 12)
iM=np.linspace(-30, 35, num=200)
plt.hist(pz2, iM)
plt.xlabel('P2 Z Momentum (GeV/c)')

## DiMuon INVARIANT MASS - LOOP OVER THE EVENTS
    #
    # For each event calculate the DiMuon System's Energy (Esys),
    # 3-momentum (P3sys=[Px,Py,Pz]) and invariant mass
    #
Esys=[]
Psys=[]
InvMass=[]
for x in range(0, nP):
    newEsys=E1[x]+E2[x]
    Esys.append(newEsys)
    newPx=px1[x]+px2[x]
    newPy=py1[x]+py2[x]
    newPz=pz1[x]+pz2[x]
    newPsys=newPx**2+newPy**2+newPz**2
    Psys.append(newPsys)
    newInvMass=math.sqrt(newEsys**2-newPsys)
    InvMass.append(newInvMass)
        
plt.figure(2)

tM = np.linspace(0, 115, num=300)
plt.hist(InvMass, tM)
plt.yscale("log")
plt.xlabel('Mass (GeV/$c^2$)')

B = []
for x in range(0, nP):
    newPx=px1[x]+px2[x]
    newPy=py1[x]+py2[x]
    newPz=pz1[x]+pz2[x]
    
    Esys=E2[x]+E1[x]
    Bx=newPx/Esys
    By=newPy/Esys
    Bz=newPz/Esys
    
    #
    # Calculate Bsys, B and Gam for the current event
    #B=momentum/energy
    
    Bsq=Bx**2+By**2+Bz**2
    sqrtB=math.sqrt(Bsq)
    B.append(sqrtB)
    
sameB = []
oppB = []
for x in range(0, nP):
    if Charge1[x] != Charge2[x]:
        oppB.append(B[x])
    else:
        sameB.append(B[x])
        
#graphs of the diMuon velocity with same signs and opposite signs        
        
plt.figure(3)

oM = np.linspace(0, 1, num=500)
plt.subplot(1, 2, 1)
plt.hist(oppB, oM)
plt.xlabel('Opposite Sign DiMuon Velocity')
plt.yscale("log")

plt.subplot(1, 2, 2)
plt.hist(sameB, oM)
plt.xlabel('Same Sign DiMuon Velocity')
plt.yscale("log")

plt.figure(4)

pM = np.linspace(0, .1, num=200)
plt.hist(oppB, pM)
plt.xlabel('Opposite Sign DiMuon Velocity <= 0.1')

#find the muon quality of the cosmic rays

MuQualCos = []
for x in range(0, nP):
    if B[x] <= .03:
        if Charge1[x] == Charge2[x]:
            newMuQualCos = 0
        elif Type[x] == 'GT':
            newMuQualCos = 2
        else:
            newMuQualCos = 3
        MuQualCos.append(newMuQualCos)
   
# a histogram of the muon quality of the cosmic rays
     
plt.figure(5)

aM = np.linspace(0, 3, num = 25)
plt.hist(MuQualCos, aM)
plt.xlabel('Quality of Particles with Velocity <= 0.03')

#scatter plots of phi vs eta for all of the muons

plt.figure(6)

plt.subplot(1, 2, 1)
plt.scatter(eta1, phi1, s=0.1, c='b')
plt.xlabel('Eta')
plt.ylabel('Phi (Rads)')
plt.title('Muon 1')

plt.subplot(1, 2, 2)
plt.scatter(eta2, phi2, s=0.1, c='r')
plt.xlabel('Eta')
plt.ylabel('Phi (Rads)')
plt.title('Muon 2')

#separate the cosmic eta and phi values from the rest of the data

coseta1 = []
cosphi1 = []
coseta2 = []
cosphi2 = []
for x in range(0, nP):
    if B[x] <= .03:
        coseta1.append(eta1[x])
        cosphi1.append(phi1[x])
        coseta2.append(eta2[x])
        cosphi2.append(phi2[x])

#scatter plots of phi vs eta of the cosmic rays

plt.figure(7)

plt.subplot(1, 2, 1)
plt.scatter(coseta1, cosphi1, s=0.1, c='b')
plt.xlabel('Eta')
plt.ylabel('Phi (Rads)')
plt.title('Muon 1')

plt.subplot(1, 2, 2)
plt.scatter(coseta2, cosphi2, s=0.1, c='r')
plt.xlabel('Eta')
plt.ylabel('Phi (Rads)')
plt.title('Muon 2')

#separate the cosmic particles from the rest of the muons
cosInvMass = []
notcosInvMass = []
notcosMuQuality = []
for x in range (0, nP):
    if B[x] <= .03:
        cosInvMass.append(InvMass[x])
    else:
        notcosInvMass.append(InvMass[x])
        notcosMuQuality.append(MuQuality[x])
        
#Graphs of the mass of the cosmic particles up close
        
plt.figure(8)

xM = np.linspace(0, 20, num=100)
plt.hist(cosInvMass, xM)
plt.xlabel('Mass of Cosmic Particles (GeV/$c^2$)')

plt.figure(9)

xM1 = np.linspace(12, 80, num=100)
plt.hist(cosInvMass, xM1)
plt.xlabel('Mass of Cosmic Particles (GeV/$c^2$)')

plt.figure(10)

xM2 = np.linspace(80, 115, num=100)
plt.hist(cosInvMass, xM2)
plt.xlabel('Mass of Cosmic Particles (GeV/$c^2$)')


#find the masses of the particles at different muon quality
notcosInvMassG1=[]
notcosInvMassG2=[]
notcosInvMassG3=[]

for x in range(0, len(notcosInvMass)):
    if notcosMuQuality[x]>=1:
        notcosInvMassG1.append(notcosInvMass[x])
    if notcosMuQuality[x]>=2:
        notcosInvMassG2.append(notcosInvMass[x])
    if notcosMuQuality[x]>=3:
        notcosInvMassG3.append(notcosInvMass[x])
        
#
#Graphs of the mass of the non-cosmic particles with different muon quality
#

plt.figure(11)

plt.subplot(2,2,1)
xM3 = np.linspace(0, 115, num=200)
plt.hist(notcosInvMass, xM3)
plt.xlabel('Mass of non-Cosmic Particles (GeV/$c^2$)')
plt.yscale("log")

plt.subplot(2,2,2)
plt.hist(notcosInvMassG1, xM3)
plt.xlabel('Mass of non-Cosmic Particles with Quality >= 1 (GeV/$c^2$)')
plt.yscale("log")

plt.subplot(2,2,3)
plt.hist(notcosInvMassG2, xM3)
plt.xlabel('Mass of non-Cosmic Particles with Quality >= 2 (GeV/$c^2$)')
plt.yscale("log")

plt.subplot(2,2,4)
plt.hist(notcosInvMassG2, xM3)
plt.xlabel('Mass of non-Cosmic Particles with Quality >= 3 (GeV/$c^2$)')
plt.yscale("log")
