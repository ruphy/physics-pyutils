
from ROOT import gInterpreter, gSystem, TFile, gDirectory, gDebug
from os import popen

class TreeHandler:

    _treeName = ''
    _fileName = ''
    _entries = ''
    _mychain = ''

    def __init__(self, filename, treename):
        gDebug = 7
        #gSystem.AddLinkedLibs(popen('root-config --libs').read())
        #gSystem.SetInclude(popen('root-config --include').read());
        gInterpreter.GenerateDictionary("vector<ROOT::Math::Cartesian3D<double> >", "Math/Cartesian3D.h")
        self._fileName = filename
        self._treeName = treename

        myfile = TFile(self._fileName)
        self._mychain = gDirectory.Get(self._treeName)
        self._entries = self._mychain.GetEntriesFast()


    def __getattr__(self, attr):
        data = []
        for jentry in xrange(self._entries):
            self._mychain.GetEntry(jentry)
            data.append(self._mychain.attr)
        return data


