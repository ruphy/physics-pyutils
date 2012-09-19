
from pyphysics.histomanager import HistoManager
from pyphysics.treehandler import TreeHandler
from ROOT import gInterpreter
import numpy as np

gInterpreter.GenerateDictionary('"vector<ROOT::Math::Cartesian3D<double> >", "Math/Cartesian3D.h");')

def funz(P, x):
    return P[0]*np.exp(-x/P[1])

t = TreeHandler('out.root', 'tree')

h = HistoManager()
h.set_data(t.AbsLength)
h.set_initial_guess([1,1])
h.set_func(funz)
h.fit_and_draw()
h.save()
    
