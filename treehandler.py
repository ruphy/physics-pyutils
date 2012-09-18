
from ROOT import gInterpreter, gSystem, TFile, gDirectory, gDebug
from os import popen

class TreeHandler:

    _treeName = ""
    _fileName = ""

    def __init__(self, filename, treename):
        self._fileName = filename
        self._treeName = treename

    def __getattr__(self, attr):
        data = []

        _f = TFile(self._fileName)
        _chain = gDirectory.Get(self._treeName)
        _entries = _chain.GetEntriesFast()

        for jentry in xrange(_entries):
            _chain.GetEntry(jentry)
            data.append(_chain.__getattr__(attr))
        return data


