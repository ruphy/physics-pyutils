
from ROOT import gInterpreter, gSystem, TFile, gDirectory

class TreeHandler:

    _treeName = ''
    _fileName = ''
    _entries = ''
    _mychain = ''

    def __init__(self, filename, treename):
        gSystem.AddLinkedLibs(popen('root-config --libs').read())
        gInterpreter.GenerateDictionary("vector<ROOT::Math::Cartesian3D<double> >", "Math/Cartesian3D.h")
        _fileName = filename
        _treeName = treename

        myfile = TFile(_fileName)
        _mychain = gDirectory.Get(_treeName)
        _entries = mychain.GetEntriesFast()


    def __getattr__(self, attr):
        data = []
        for jentry in xrange(_entries):
            _mychain.GetEntry(jentry)
            data.append(_mychain.attr)
        return data


