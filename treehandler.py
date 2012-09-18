
from ROOT import gInterpreter, gSystem, TFile, gDirectory, gDebug
from os import popen

class TreeHandler:

    _treeName = ''
    _fileName = ''
    #_entries = 0
    #_mychain = ''

    def __init__(self, filename, treename):
        self._fileName = filename
        self._treeName = treename

    def __getattr__(self, attr):
        data = []

        myfile = TFile(self._fileName)
        mychain = gDirectory.Get(self._treeName)
        entries = mychain.GetEntriesFast()
        #print entries
        #for jentry in xrange(self._entries):
            #self._mychain.GetEntry(jentry)
            #data.append(self._mychain.attr)
        return data


