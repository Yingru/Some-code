
# This is the program deal with the R_AA for HIC
import numpy
import matplotlib.pyplot as plt



#R_AA for D meson in Pb+Pb collision as in the experiment result
Pt_EX, R_AA_EX,Pt1,Pt2, Rerr1, Rerr2=numpy.loadtxt('RAA_ALICE-7d5.dat', unpack=True)

#fig, axs=plt.subplots(nrows=2, ncols=2, sharex=True)
#ax=axs[0,0]
#ax.errorbar(Pt, R_AA_EX, yerr=Rerr1,ftm='0')
#ax.set_title("test1")

#ax=axs[0,1]
#ax.errorbar(Pt,R_AA, yerr=Rerr2,ftm='0')
#ax.set_title('test2')

#ax=axs[1,0]
#ax.errorbar(

plt.figure()
plt.errorbar(Pt_EX, R_AA_EX, yerr=Rerr1, color='r')
plt.errorbar(Pt_EX, R_AA_EX, yerr=Rerr2,color='b')

plt.show()
