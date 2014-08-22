# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:35:39 2014

@author: Yingru
"""

# This is the program deal with the R_AA for HIC
import numpy
import matplotlib.pyplot as plt

#R_AA for D meson in Pb+Pb collision as in my initial momentum
Pt_YX, PbCY_YX=numpy.loadtxt('multi_PbCY_LHC_0-7d5_hardon.dat', unpack=True, usecols=[0,1])
Pt2_YX, PbCN_YX=numpy.loadtxt('multi_PbCN_LHC_0-7d5_hardon.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision as in Shanshan's initial momentum
Pt_SC, PbCY_SC=numpy.loadtxt('multi_AACY_hadron.dat', unpack=True, usecols=[0,1])
Pt2_SC, PbCN_SC=numpy.loadtxt('multi_AACN_hadron.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision as in the experiment result
Pt_EX, R_AA_EX=numpy.loadtxt('RAA_ALICE-7d5.dat', unpack=True, usecols=[0,1])


#R_AA for Charm quark before hadronization
Pt, PbCY=numpy.loadtxt('multi_AuCY_LHC_0-7d5.dat', unpack=True, usecols=[0,1])
Pt2, PbCN=numpy.loadtxt('multi_AuCN_LHC_0-7d5.dat', unpack=True, usecols=[0,1])


R_AA_YX=[0.0]*0
R_AA_SC=[0.0]*0
R_AA=[0.0]*0

for i in range(25):
    R_AA_YX.append(1.3581/2.6602*PbCY_YX[i]/PbCN_YX[i])
    R_AA_SC.append(0.6843/1.4853*PbCY_SC[i]/PbCN_SC[i])
    R_AA.append(0.6843/1.4853*PbCY[i]/PbCN[i])
    
#DataOut= numpy.column_stack((Pt, R_AA)) 

plt.plot(Pt, R_AA_YX, '--bo', color='blue', linewidth=2.5, label='R_AA for D meson (YX)')
plt.plot(Pt, R_AA_SC, '-', color='red', linewidth=2.5, label='R_AA for D meson (SC)')
#plt.plot(Pt, R_AA_EX, '-', color='purple', linewidth=2.5, label="R_AA for D meson (ALICE)")
plt.plot(Pt, R_AA, '--', color='green', linewidth=2.5, label='R_AA for Charm quark')
plt.xlabel('Pt')
plt.ylabel('R_AA')
plt.legend(loc='upper right')
plt.title("R_AA in Pb+Pb collision")
plt.show()
    
numpy.savetxt('YX_R_AA_1.dat', (Pt, R_AA))
    
    
