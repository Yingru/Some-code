# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:35:39 2014

@author: Yingru
"""

# This is the program deal with the R_AA for HIC
import numpy
import matplotlib.pyplot as plt

#R_AA for D meson in Pb+Pb collision in my initial momentum, (coefficient =6.5)
Pt_6d5, PbCY_6d5=numpy.loadtxt('multi_PbCY_6d5.dat', unpack=True, usecols=[0,1])
Pt2_6d5, PbCN_6d5=numpy.loadtxt('multi_PbCN_6d5.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision as in my initial momentum, (coefficient =6.0)
Pt_YX, PbCY_YX=numpy.loadtxt('multi_PbCY_6_YX.dat', unpack=True, usecols=[0,1])
Pt2_YX, PbCN_YX=numpy.loadtxt('multi_PbCN_6_YX.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision as in Shanshan's momentum, (coefficient =6.0)
Pt_SC, PbCY_SC=numpy.loadtxt('multi_PbCY_6_SC.dat', unpack=True, usecols=[0,1])
Pt2_SC, PbCN_SC=numpy.loadtxt('multi_PbCN_6_SC.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision in my initial momentum, (coefficient =5.5)
Pt_5d5, PbCY_5d5=numpy.loadtxt('multi_PbCY_5d5.dat', unpack=True, usecols=[0,1])
Pt2_5d5, PbCN_5d5=numpy.loadtxt('multi_PbCN_5d5.dat', unpack=True, usecols=[0,1])

#R_AA for D meson in Pb+Pb collision as in the experiment result
Pt_EX, R_AA_EX,Pt1,Pt2, Rerr1, Rerr2=numpy.loadtxt('RAA_ALICE-7d5.dat', unpack=True)


R_AA_6d5=[0.0]*0
R_AA_YX=[0.0]*0
R_AA_SC=[0.0]*0
R_AA_5d5=[0.0]*0


for i in range(25):
    R_AA_6d5.append(1.3581/2.6602*PbCY_6d5[i]/PbCN_6d5[i])
    R_AA_5d5.append(1.3581/2.6602*PbCY_5d5[i]/PbCN_5d5[i])
    R_AA_YX.append(1.3581/2.6602*PbCY_YX[i]/PbCN_YX[i])
    R_AA_SC.append(0.6843/1.4853*PbCY_SC[i]/PbCN_SC[i])
    

#DataOut= numpy.column_stack((Pt, R_AA)) 

plt.figure()
plt.plot(Pt_6d5, R_AA_6d5, '--',color='r', linewidth=2.5, label='R_AA for D meson (6.5)')
plt.plot(Pt_YX, R_AA_YX, '--', color='m' , linewidth=2.5, label='R_AA for D meson (6.0)')
plt.plot(Pt_5d5, R_AA_5d5, '--', color='blue' ,linewidth=2.5, label='R_AA for D meson (5.5)')
plt.plot(Pt_SC, R_AA_SC, '-', color='green' ,linewidth=2.5, label='R_AA for D meson (SC)')
plt.errorbar(Pt_EX, R_AA_EX, yerr=[Rerr1,Rerr2],fmt='o',color='black',ecolor='black',capthick=2, label='R_AA for D meson (ALICE)')
plt.xlabel('Pt')
plt.ylabel('R_AA')
plt.legend(loc='upper right')
plt.title("R_AA in Pb+Pb collision")
plt.show()
    

    
    
