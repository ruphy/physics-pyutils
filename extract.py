# Aggiungi qui, separandole da virgole, le classi di ROOT
# che usi:
from os import popen
from treehandler import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import odr
from re import sub
from ROOT import gInterpreter, gSystem, TFile, gDirectory, gROOT

popen('root -l -q -b -n dict.cpp 2> /dev/null').read()
print "finished root"
#gROOT.ProcessLine('.x dict.cpp')

# ---------------------- #
# Inizio codice serio    #
# ---------------------- #

def run_sim(nm):
    #ev = 1239.84/nm
    ## sub the new energy in the file
    #with open('gps.mac','r') as f:
        #newlines = []
        #for line in f.readlines():
            #newlines.append(sub(r'/gps/energy.*', '/gps/energy %.3f eV' % ev, line))
    #with open('gps.mac', 'w') as f:
        #for line in newlines:
            #f.write(line)
    ## run the simulation
    #popen('./crystal crystal.cfg')

    # open the tree file
    #myfile = TFile( 'out.root' )
    #print "building treehandler"
    t = TreeHandler('out.root', 'tree')
    #print "returning"
    #print t.AbsLength
    #return
    # retrieve the ntuple of interest
    #mychain = gDirectory.Get( 'tree' )
    #entries = mychain.GetEntriesFast()

    #data = []

    #for jentry in xrange( entries ):
        #mychain.GetEntry( jentry )
        #data.append(mychain.AbsLength)

    #def funz(P, x):
        #return P[1]*np.exp(-x/P[0])


        plt.title(r"Mean absorption length (%dnm): $\lambda=$ %.1f mm" % (nm, param[0]))

nms = [420, 470, 500];

for i in nms:
    run_sim(i)


# ----------- #
# Fine codice #
# ----------- #

# HACK!!!
# Non modificare il codice sotto questa riga:
# serve a gestire correttamente la finestra di root
#import sys
#from Tkinter import Tk

#def check_quit():
  #try:
    #a = c1.GetWindowWidth()
    #root.after(500, check_quit)
  #except AttributeError:
    #sys.exit()

#root = None # invisible tk window
#root = Tk()
#root.withdraw()
#root.after(1, check_quit)
#root.mainloop()

