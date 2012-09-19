# Aggiungi qui, separandole da virgole, le classi di ROOT
# che usi:
from os import system
from treehandler import *
from histomanager import *
import numpy as np
import matplotlib.pyplot as plt
from scipy import odr
from re import sub
from ROOT import gInterpreter, gSystem, TFile, gDirectory, gROOT

system('root -l -q -b -n dict.cpp 2> /dev/null')

def funz(P, x):
    return P[0]*np.exp(-x/P[1])

t = TreeHandler('out.root', 'tree')
data = t.AbsLength
h = HistoManager()
h.set_data(data)
h.set_initial_params([8000,1850])
h.set_func(funz)
h.fit_and_draw()
h.save()
    
