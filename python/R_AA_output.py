#This is a program which can output the R_AA
    
import numpy

#load file for multiplicity
Pt_AA, AA=numpy.loadtxt("multi_E_AAcY.dat", unpack=True, usecols=[0,1])
Pt_pp, pp=numpy.loadtxt("multi_E_AAcN.dat", unpack=True, usecols=[0,1])
Pt_AA_cronin, AA_cronin=numpy.loadtxt("multi_E_AAcY_cronin.dat", unpack=True, usecols=[0,1])

Pt_AA_2, AA_2=numpy.loadtxt("multi_E_AAbY.dat", unpack=True, usecols=[0,1])
Pt_pp_2, pp_2=numpy.loadtxt("multi_E_AAbN.dat", unpack=True, usecols=[0,1])
Pt_AA_cronin_2, AA_cronin_2=numpy.loadtxt("multi_E_AAbY_cronin.dat", unpack=True, usecols=[0,1])

R_AA=[0.0]*0
R_AA_cronin=[0.0]*0

for i in range(15):
 #  R_AA.append((2.2353*AA[i])/(2.0317*pp[i]))
 #  R_AA_cronin.append((2.2353*AA_cronin[i])/(2.0317*pp[i]))
   R_AA.append((8.1182*10e-2*AA[i]+2.2353*10e-4*AA_2[i])/(7.2604*10e-2*pp[i]+2.0317*10e-4*pp_2[i]))       
   R_AA_cronin.append((8.1182*10e-2*AA_cronin[i]+2.2353*10e-4*AA_cronin_2[i])/(7.2604*10e-2*pp[i]+2.0317*10e-4*pp_2[i]))
numpy.savetxt('R_E_model.dat', numpy.transpose([Pt_AA, R_AA]))   
numpy.savetxt('R_E_model_cronin.dat', numpy.transpose([Pt_AA, R_AA_cronin]))   
# you can also use numpy.savetxt('output.txt', numpy.c_[Pt_AA, R_AA])
# also , numpy.savetxt('test.dat', numpy.column_stack((Pt, R_AA)))

