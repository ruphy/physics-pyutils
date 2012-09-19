# Aggiungi qui, separandole da virgole, le classi di ROOT
# che usi:
from treehandler import *
from histomanager import *
from ROOT import gInterpreter

gInterpreter.GenerateDictionary('"vector<ROOT::Math::Cartesian3D<double> >", "Math/Cartesian3D.h");')

def funz(P, x):
    return P[0]*np.exp(-x/P[1])

t = TreeHandler('out.root', 'tree')

h = HistoManager()
h.set_data(t.AbsLength)
h.set_func(funz)
h.fit_and_draw()
h.save()
    
