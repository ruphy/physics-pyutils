import matplotlib.pyplot as plt
import scipy.odr as odr
import numpy as np

class HistoManager:
    _func = None
    _data = None
    _initial_params = None
    _title = "Title"
    _xlabel = "Data on x"
    _ylabel = "Data on y"
    _fitted_params = None

    def __init__(self):
        self.clear()
        plt.title(self._title)
        plt.ylabel(self._ylabel)
        plt.xlabel(self._xlabel)

    def clear(self):
        plt.clf()

    def set_data(self, data):
        self._data = data

    def set_func(self, func):
        self._func = func

    def set_initial_params(self, params):
        self._initial_params = params

    def set_xlabel(self, xlabel):
        self._xlabel = xlabel
        plt.xlabel(self._xlabel)

    def set_ylabel(self, ylabel):
        self._ylabel = ylabel
        plt.ylabel(self._ylabel)

    def set_title(self, title):
        self._title = title
        plt.title(self._title)

    def get_fitted_params(self):
        return self._fitted_params
    
    def fit_and_draw(self, nbins=100):
        plt.grid(True)

        (n, bins, patches) = plt.hist(self._data, nbins, color='#50e300', alpha=.7)
        bins = 0.5*(bins[:-1] + bins[1:])

        xdata = bins
        ydata = n

        mymodel = odr.Model(self._func)
        mydata = odr.RealData(xdata, ydata) #, sx=(bins[0]-bins[1])/2, sy=0.001)
        if (self._initial_params):
            myodr = odr.ODR(mydata, mymodel, beta0=self._initial_params, maxit=10000)
        else:
            myodr = odr.ODR(mydata, mymodel, maxit=10000)

        myoutput = myodr.run()
        myoutput.pprint()

        xdata = np.arange(min(bins), max(bins))
        ydata = self._func(myoutput.beta, xdata)
        plt.plot(xdata, ydata)

        self._fitted_params = myoutput.beta
        return self._fitted_params

    def save(self, outfile="out.png"):
        plt.savefig(outfile)


