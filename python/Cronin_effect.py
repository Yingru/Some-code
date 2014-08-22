#This is a program which deals with the cronin effect, it will result the shift in Pt distribution.

import numpy
import matplotlib.pyplot as plt
import csv

#load data
Pt, AAcY=numpy.loadtxt('RHIC_AuAu2bbar.dat', unpack=True, usecols=[0,1])
a=0.0359115
c=0.0004380525
d=-1.79274e-6
e=0.215603
f=-0.00493175
g=0.0000263330
h=9.19488e-7
dPt=0.5
delta=0.2
b=0

Ncoll=(1+(a+(c+d*b**2)*b**2)*b**2)/(e+(f+(g+h*b**2)*b**2)*b**2)

AAcY_new=[0.0]*140
#conduct the gaussian expansion on the data


for i in range(62):
    norm=0
    fPt=0
    for j in range(62):
        fPt+=AAcY[j]*numpy.exp(-(Pt[i]-Pt[j])**2*e/delta)*dPt
        norm+=numpy.exp(-(Pt[i]-Pt[j])**2*e/delta)*dPt
    AAcY_new[i]=fPt

cross_section=0.0
for i in range(62):
    cross_section+=Pt[i]*AAcY[i]

cross_section_cronin=0.0
for i in range(62):
    cross_section_cronin+=Pt[i]*AAcY_new[i]

for i in range(62):
    AAcY_new[i]=AAcY_new[i]*cross_section/cross_section_cronin

        

numpy.savetxt('RHIC_AuAu2bbar_cronin.dat', numpy.column_stack((Pt, AAcY_new)))

