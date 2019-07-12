#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:25:44 2019

@author: QuarkNet
"""

# 0=same charge  <--rule out this
# 1=both Tracker
# 2=one Global one Tracker
# 3=both Global

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

xM=np.linspace(1.5, 5.5, num=200)
nP=2000


data_path = 'QuarknetMuonData - Sheet1.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    # get header from first row
    headers = next(reader)
    # get all the rows as a list
    data = list(reader)
    # transform data into numpy array
    data = np.array(data).astype(float)


EvtNum = data[:, 1]

MuQuality = data[:, 2]

E1 = data[:, 3]
px1 = data[:, 4]
py1 = data [:, 5]
pz1 = data[:, 6]

E2 = data[:, 7]
px2 = data[:, 8]
py2 = data [:, 9]
pz2 = data[:, 10]

## INITIALIZE SOME ARRAYS TO ZERO




## DIAGNOSTICS

#
# Diagnostic Plots: Histogram all 10 input variables
# in one Figure using subplots
#

plt.figure(1)

plt.subplot(3, 4, 2)
plt.hist(EvtNum)
plt.title('Event Number')

plt.subplot(3, 4, 3)
plt.hist(MuQuality)
plt.title('Muon Quality')

plt.subplot(3, 4, 5)
cM=np.linspace(0, 45, num=100)
plt.hist(E1, cM)
plt.title('Particle 1 Energy')

plt.subplot(3, 4, 6)
dM=np.linspace(-10, 10, num=100)
plt.hist(px1, dM)
plt.title('P1 X Momentum')

plt.subplot(3, 4, 7)
eM=np.linspace(-16, 12.5, num=100)
plt.hist(py1, eM)
plt.title('P1 Y Momentum')

plt.subplot(3, 4, 8)
fM=np.linspace(-55, 50, num=100)
plt.hist(pz1, fM)
plt.title('P1 Z Momentum')


plt.subplot(3, 4, 9)
gM=np.linspace(0, 30, num=100)
plt.hist(E2, gM)
plt.title('Particle 2 Energy')

plt.subplot(3, 4, 10)
hM=np.linspace(-10, 10, num=100)
plt.hist(px2, hM)
plt.title('P2 X Momentum')

plt.subplot(3, 4, 11)
plt.hist(py2, hM)
plt.title('P2 Y Momentum')

plt.subplot(3, 4, 12)
iM=np.linspace(-45, 35, num=100)
plt.hist(pz2, iM)
plt.title('P2 Z Momentum')


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
    

#
# Histogram Esys, Psys (the magnitude of the 3-momentum)and the DiMuon
# invariant mass in one Figure using subplots
#
    
plt.figure(2)

plt.subplot(1, 3, 1)
zM=np.linspace(5, 55, num=100)
plt.hist(Esys, zM)
plt.title('Energy of the System')

plt.subplot(1, 3, 2)
yM =np.linspace(150,1500, num=100)
plt.hist(Psys, yM)
plt.title('Momentum of the System')

plt.subplot(1, 3, 3)
plt.hist(InvMass, xM)
plt.title('Invariant Mass')



## INVESTIGATE THE IMPACT OF IMPOSING MuQuality SELECTIONS CRITERIA (CUTS)
# ON THE DiMuon INVARIANT MASS DISTRIBUTION

#
# Histogram the DiMuon invariant mass for MuQuality >=0, MuQuality >=1,
# MuQuality >=2 and MuQuality >=3. Arrange the four histograms in
# one Figure using subplots.
#

InvMassG1=[]
InvMassG2=[]
InvMassG3=[]


for x in range(0, nP):
    if MuQuality[x]>=1:
        InvMassG1.append(InvMass[x])
        
    if MuQuality[x]>=2:
        InvMassG2.append(InvMass[x])
        
    if MuQuality[x]>=3:
        InvMassG3.append(InvMass[x])
        
        
plt.figure(3)

plt.subplot(2, 2, 1)
plt.hist(InvMass, xM)
plt.title('Invariant Mass')

plt.subplot(2, 2, 2)
plt.hist(InvMassG1, xM)
plt.title('Invariant Mass w/ Quality>=1')

plt.subplot(2, 2, 3)
plt.hist(InvMassG2, xM)
plt.title('Invariant Mass w/ Quality>=2')

plt.subplot(2, 2, 4)
plt.hist(InvMassG3, xM)
plt.title('Invariant Mass w/ Quality>=3')       


## FOR EACH EVENT TRANSFORM TO THE REST FRAME OF THE DiMuon SYSTEM
# 1. TO CALCULATE THE DiMuon INVARIANT MASS IN THE REST FRAME
# 2. TO INVESTIGATE THE RELATIONSHIPS BETWEEN THE COMPONENTS OF THE
# 4-MOMENTUM OF THE FIRST MUON, [E1,px1,py1,pz1], WITH THAT OF THE
# SECOND MUON, [E2,px2,py2,pz2], IN THE REST FRAME
#

#
# For the Lorentz Transformation ( http://en.wikipedia.org/wiki/Lorentz_transformation )
# we need to calculate the following quantities for the DiMuon Rest Frame:
# The DiMuon system's velocity: Bsys=(Bx,By,Bz)=P3sys/Esys;
# B=sqrt(Bx^2+By^2+Bz^2) and Gam=sqrt(1/(1-B^2))
#

## TRANSFORM TO THE DiMuon REST FRAME - LOOP OVER THE EVENTS

EsysRF=[]
PsysRF=[]
InvMassRF=[]
px1RF=[]
py1RF=[]
pz1RF=[]
px2RF=[]
py2RF=[]
pz2RF=[]
E1RF=[]
E2RF=[]
# beginning of loop over the events
for x in range(0, nP):
    newPx=px1[x]+px2[x]
    newPy=py1[x]+py2[x]
    newPz=pz1[x]+pz2[x]
    
    E1i=E1[x]
    E2i=E2[x]
    #
    # Calculate Esys and P3sys for the current event
    #
    Esysi=E2i+E1i
    Bx=newPx/Esysi
    By=newPy/Esysi
    Bz=newPz/Esysi
    
    #
    # Calculate Bsys, B and Gam for the current event
    #B=momentum/energy
    
    
    Bsq=Bx**2+By**2+Bz**2
    Gam=1/math.sqrt(1-Bsq)
    
    #
    # Create the 4x4 Lorentz Transformation Matrix that will
    # allow us to transform the 4-momentum, [E,px,py,pz], of each of the muons
    # from the Lab Frame (where they were measured) to the Rest Frame of the
    # DiMuon system.
    #
    
    L=np.array([[Gam,-Gam*Bx,-Gam*By,-Gam*Bz],[-Gam*Bx,1+(Gam-1)*(Bx**2/Bsq),(Gam-1)*(Bx*By/Bsq),(Gam-1)*(Bx*Bz/Bsq)],[-Gam*By,(Gam-1)*(By*Bx/Bsq),1+(Gam-1)*(By**2/Bsq),(Gam-1)*(By*Bz/Bsq)],[-Gam*Bz, (Gam-1)*(Bz*Bx/Bsq),(Gam-1)*(Bz*By/Bsq),1+(Gam-1)*(Bz**2/Bsq)]])
    Mu1=np.array([[E1i],[px1[x]],[py1[x]],[pz1[x]]])
    Mu2=np.array([[E2i],[px2[x]],[py2[x]],[pz2[x]]])
    
    #
    # Transform Mu1 and Mu2 from the Lab Frame to the DiMuon Rest Frame
    # to yield Mu1RF and Mu2RF (RF means DiMuon Rest Frame)
    #
    
    Mu1RF=np.matmul(L,Mu1)
    Mu2RF=np.matmul(L,Mu2)
    
    E1RF.append(Mu1RF[0][0])
    E2RF.append(Mu2RF[0][0])
    
    #
    # calculate EsysRF, P3sysRF
    # and the DiMuon invariant mass in the DiMuon Rest Frame.
    # calculate EsysRF, P3sysRF
    # and the DiMuon invariant mass in the DiMuon Rest Frame.
    #
    
    newEsysRF=Mu1RF[0][0] + Mu2RF[0][0]
    EsysRF.append(newEsysRF)
    newPxRF=Mu1RF[1][0] + Mu2RF[1][0]
    px1RF.append(Mu1RF[1][0])
    px2RF.append(Mu2RF[1][0])
    newPyRF=Mu1RF[2][0] + Mu2RF[2][0]
    py1RF.append(Mu1RF[2][0])
    py2RF.append(Mu2RF[2][0])
    newPzRF=Mu1RF[3][0] + Mu2RF[3][0]
    pz1RF.append(Mu1RF[3][0])
    pz2RF.append(Mu1RF[3][0])
    newPsysRF=newPxRF**2+newPyRF**2+newPzRF**2
    PsysRF.append(newPsysRF)
    newInvMassRF=math.sqrt(newEsysRF**2-newPsysRF)
    InvMassRF.append(newInvMassRF)
    # end of loop over the events
    
## Histograms    
#
# Diagnostic Plots: Histogram all 10 input variables
# in the DiMuon Rest Frame in one Figure using subplots
    
plt.figure(4)

plt.subplot(3, 4, 2)
plt.hist(EvtNum)
plt.title('Event Number')

plt.subplot(3, 4, 3)
plt.hist(MuQuality)
plt.title('Muon Quality')

plt.subplot(3, 4, 5)
jM=np.linspace(0.9, 2.5, num=100)
plt.hist(E1RF, jM)
plt.title('Particle 1 Energy Rest Frame')

plt.subplot(3, 4, 6)
kM=np.linspace(-2.5, 2.5, num=100)
plt.hist(px1RF, kM)
plt.title('P1 X Momentum Rest Frame')

plt.subplot(3, 4, 7)
plt.hist(py1RF, kM)
plt.title('P1 Y Momentum Rest Frame')

plt.subplot(3, 4, 8)
lM=np.linspace(-2, 2, num=100)
plt.hist(pz1RF, lM)
plt.title('P1 Z Momentum Rest Frame')


plt.subplot(3, 4, 9)
plt.hist(E2RF, jM)
plt.title('Particle 2 Energy Rest Frame')

plt.subplot(3, 4, 10)
hM=np.linspace(-10, 10, num=100)
plt.hist(px2RF, kM)
plt.title('P2 X Momentum Rest Frame')

plt.subplot(3, 4, 11)
plt.hist(py2RF, kM)
plt.title('P2 Y Momentum Rest Frame')

plt.subplot(3, 4, 12)
plt.hist(pz2RF, lM)
plt.title('P2 Z Momentum Rest Frame')

#
# Histogram Esys, Psys (the magnitude of the 3-momentum)and the invariant
# mass of the DiMuon System in the DiMuon Rest Frame in one Figure using
# subplots

plt.figure(5)

plt.subplot(1, 3, 1)
wM=np.linspace(1.9, 5.1, num=100)
plt.hist(EsysRF, wM)
plt.title('Energy of the System Rest Frame')

plt.subplot(1, 3, 2)
sM=np.linspace(-1e-30, .8e-28, num=100)
plt.hist(PsysRF, sM)
plt.title('Momentum of the System Rest Frame')

plt.subplot(1, 3, 3)
plt.hist(InvMassRF, wM)
plt.title('Invariant Mass Rest Frame')

#
# Histogram the DiMuon Invariant mass in the DiMuon Rest Frame
# for MuQuality >=0, MuQuality >=1, MuQuality >=2 and MuQuality >=3.
# Arrange the four histograms in one Figure using subplots
#

InvMassG1RF=[]
InvMassG2RF=[]
InvMassG3RF=[]

for x in range(0, nP):
    if MuQuality[x]>=1:
        InvMassG1RF.append(InvMassRF[x])
        
    if MuQuality[x]>=2:
        InvMassG2RF.append(InvMassRF[x])
        
    if MuQuality[x]>=3:
        InvMassG3RF.append(InvMassRF[x])
        
plt.figure(6)

plt.subplot(2, 2, 1)
vM=np.linspace(2, 5, num=200)
plt.hist(InvMassRF, vM)
plt.title('Invariant Mass')

plt.subplot(2, 2, 2)
plt.hist(InvMassG1RF, vM)
plt.title('Invariant Mass w/ Quality>=1 Rest Frame')

plt.subplot(2, 2, 3)
plt.hist(InvMassG2RF, vM)
plt.title('Invariant Mass w/ Quality>=2 Rest Frame')

plt.subplot(2, 2, 4)
plt.hist(InvMassG3RF, vM)
plt.title('Invariant Mass w/ Quality>=3 Rest Frame')
