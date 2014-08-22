#This is a program to plot the experimental data and model data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

#load data from file
Pt_EX, R_EX, Pterr1, Pterr2, Rerr1, Rerr2 =np.loadtxt('RHIC_62.dat', unpack=True)

#load data from file (experiment data)
Pt_EX_2, R_EX_2, Pt_2err1, Pt_2err2, R_2err1, R_2err2 =np.loadtxt('RHIC_62_2.dat', unpack=True)

#load data from file (theory data)
Pt, R=np.loadtxt('R_E_model.dat', unpack=True)

#load data from file (theory data including cronin effect)
Pt_cronin, R_cronin=np.loadtxt('R_E_model_cronin.dat', unpack=True)

fig = plt.figure()
for i in range(36):
    xy=Pt_EX[i]-Pterr1[1], R_EX[i]-Rerr1[i]
    width, height = Pterr1[i]+Pterr2[i], Rerr1[i]+Rerr2[i]
    p=patches.Rectangle(xy, width, height, facecolor='none', edgecolor='blue')
    plt.gca().add_patch(p)
    plt.draw()
    #verts=[(Pt_EX[i]-Pterr1[i], R_EX[i]-Rerr1[i]), (Pt_EX[i]+Pterr2[i], R_EX[i]-Rerr1[i]), (Pt_EX[i]-Pterr1[i], R_EX[i]+Rerr2[i]), (Pt_EX[i]+Pterr2[i], R_EX[i]+Rerr2[i]), (Pt_EX[i], R_EX[i])]
    #codes=[Path.MOVETO, Path.LINETO, Path.LINETO,Path.LINETO, Path.CLOSEPOLY]
    #path=Path(verts, codes)
    #ax=fig.add_subplot(111)
    #patch = patches.PathPatch(path, facecolor='orange', lw=2)
    #ax.add_patch(patch)
    

#plt.errorbar(Pt_EX, R_EX, color='black', xerr=[Pterr1, Pterr2],  yerr=[Rerr1, Rerr2], fmt=' ',ecolor='green')
plt.errorbar(Pt_EX_2, R_EX_2, color='black', yerr=[R_2err1, R_2err2], fmt='o',ecolor='green', label='ALICE reference')
plt.plot(Pt_cronin, R_cronin, "-", lw=2.5, color='cyan', label='R_pPb for electron, with cronin effect')
plt.plot(Pt, R, "--", lw='2.5',color='red', label='R_pPb for electron')
#plt.plot(Pt_cronin, R_cronin, "--", lw=2.5, color='cyan', label='R_pPb for electron, with cronin effect')
plt.legend(loc='upper left')
plt.xlabel('Pt(GeV/c)')
plt.ylabel('R_pPb for electron')
plt.xlim([0,5.4])
plt.ylim([0,4.0])
plt.title('Modification factor in Au+Au collision at 62.4 GeV')
plt.show()
