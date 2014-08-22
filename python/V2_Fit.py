# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:35:39 2014

@author: Yingru
"""

# This is the program deal with the R_AA for HIC
import numpy
import matplotlib.pyplot as plt

#V2 for D meson in Pb+Pb collision
Pt, V2=numpy.loadtxt('V2_PbCY_LHC_30-50.dat', unpack=True, usecols=[0,1])


#V2 for D meson in Pb+Pb collision as in the experiment result
Pt_EX, V2_EX,Pt1,Pt2, Verr1, Verr2 =numpy.loadtxt('ALICE-averageD', unpack=True)

plt.figure()
plt.plot(Pt, V2, '--',color='r', linewidth=2.5, label='V2 for D meson frag. + recomb.(6.5)')
plt.errorbar(Pt_EX, V2_EX, yerr=[Verr1,Verr2],fmt='o',color='black',ecolor='black',capthick=2, label='V2 for D meson (ALICE)')
plt.xlabel('Pt(GeV)')
plt.ylabel('V2')
plt.legend(loc='upper right')
plt.title("V2 in Pb+Pb collision")
plt.show()
