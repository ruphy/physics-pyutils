physics-pyutils
===============

Usage:

 from pyphysics.histomanager import HistoManager
 from pyphysics.treehandler import TreeHandler

 def funz(P, x):
     return P[0]*np.exp(-x/P[1])

 t = TreeHandler('out.root', 'tree')

 h = HistoManager()
 h.set_data(t.AbsLength)
 h.set_initial_guess([1,1])
 h.set_func(funz)
 h.fit_and_draw()
 h.save()
