import matplotlib.pyplot as plt
import scipy.odr as odr

class HistoManager:
    _func = None
    _data = None
    _initial_params = None
    _title = "Title"
    _xlabel = "Data on x"
    _ylabel = "Data on y"

    def __init__(self):
        print "init"

    def set_data(self, data):
        self._data = data

    def set_func(self, func):
        self._func = func

    def set_initial_params(self, params):
        self._params = params

    def set_xlabel(self, xlabel):
        self._xlabel = xlabel
        plt.xlabel(self._xlabel)

    def set_ylabel(self, ylabel):
        self._ylabel = ylabel
        plt.ylabel(self._ylabel)

    def set_title(self, title):
        self._title = title
        plt.title(self._title)
        
    def fit_and_draw(self, nbins=100):
        plt.clf()
        plt.grid(True)

        (n, bins, patches) = plt.hist(self._data, nbins, color='#50e300', alpha=.7)
        bins = 0.5*(bins[:-1] + bins[1:])

        (param, errors, cov) = odr.odr(funz, self._initial_params, n, bins)

        ydata = funz(param, np.arange(min(bins), max(bins)))
        plt.plot(np.arange(min(bins), max(bins)), ydata)

        plt.title(self._title)
        plt.ylabel(self._ylabel)
        plt.xlabel(self._xlabel)

    def save(self):
        plt.savefig("out%d.png" %nm)


