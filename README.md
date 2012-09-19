physics-pyutils
===============


How to install pyphysics:
-------------------------

Standard way - just run:

    sudo ./setup.py install

Example usage:
--------------

The code should be self-explanatory. Here is a snippet code to illustrate how it works:

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

    h.set_title("Plot title")
    h.set_xlabel("x Data")
    h.set_ylabel("y Data")
    h.save("out.png")
