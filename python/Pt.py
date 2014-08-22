 # -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:35:39 2014

@author: Yingru
"""

# This is the program deal with the R_AA for RHIC
import numpy
import matplotlib.pyplot as plt

#R_AA for electron from D meson decay in Au+Au collision at 62.4GeV
Pt_cY, AAcY_SC=numpy.loadtxt('RHIC62AA2ccbar.dat', unpack=True, usecols=[0,1])
Pt_cN, AAbY_SC=numpy.loadtxt('RHIC62AA2bbbar.dat', unpack=True, usecols=[0,1])

#R_AA for electron from B meson decay in Au+Au collision at 62.4GeV
Pt_bY, AAcY_YX=numpy.loadtxt('RHIC_AAcY.dat', unpack=True, usecols=[0,1])
Pt_bN, AAbY_YX=numpy.loadtxt('RHIC_AAbY.dat', unpack=True, usecols=[0,1])

#R_AA for electron from D meson decay in Au+Au collision at 62.4GeV
#Pt_cY_D, AAcY_D=numpy.loadtxt('multi_D_AAcY.dat', unpack=True, usecols=[0,1])
#Pt_cN_D, AAcN_D=numpy.loadtxt('multi_D_AAcN.dat', unpack=True, usecols=[0,1])

#R_AA for electron from B meson decay in Au+Au collision at 62.4GeV
#Pt_bY_B, AAbY_B=numpy.loadtxt('multi_B_AAbY.dat', unpack=True, usecols=[0,1])
#Pt_bN_B, AAbN_B=numpy.loadtxt('multi_B_AAbN.dat', unpack=True, usecols=[0,1])


#R_AA=[0.0]*0
#R_AA_c=[0.0]*0
#R_AA_b=[0.0]*0
#R_AA_D=[0.0]*0
#R_AA_B=[0.0]*0

#for i in range(15):
 #  R_AA_c.append(8.3339*AAcY[i]/(7.2604*AAcN[i]))
 #  R_AA_b.append(2.3765*AAbY[i]/(2.0317*AAbN[i]))
 # # R_AA_D.append(8.3339*AAcY_D[i]/(7.2604*AAcN_D[i]))
  # R_AA_B.append(2.3765*AAbY_B[i]/(2.0317*AAbN_B[i]))
  # R_AA.append((8.3339*10e-2*AAcY[i]+2.3765*10e-4*AAbY[i])/(7.2604*10e-2*AAcN[i]+2.0317*10e-4*AAbN[i]))
    
#DataOut= numpy.column_stack((Pt, R_AA)) 

plt.plot(Pt_cY, AAbY_SC, '-', color='green', linewidth=2.5, label='charm SC')
plt.plot(Pt_bY, AAbY_YX, '-', color='red', linewidth=2.5, label='charm YX')
#plt.plot(Pt_cY, R_AA_D, color='cyan', linewidth=2.5, label="R_AA for D meson")
#plt.plot(Pt_bY, R_AA_B, color='purple', linewidth=2.5, label="R_AA for B meson")
#plt.plot(Pt_cY, R_AA, '--', color='blue', linewidth=2.5, label='mixed')
plt.xlabel('Pt')
plt.ylabel('R_AA')
plt.legend(loc='upper right')
plt.title("R_AA in Pb+Pb collision")
plt.yscale('log')
plt.show()
    
#numpy.savetxt('YX_R_AA_1.dat', (Pt, R_AA))
    
    
