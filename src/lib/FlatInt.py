#!/usr/bin/env python

class FlatInt:
    def __init__(self, arg):
        initRange, = arg
        self.initRangeList = self.formatInitRange(initRange)
        self.generatedList = self.generate(self.initRangeList) \
                             if len(self.initRangeList)>0 else list()

    def generate(self, initRange):
        geneRange = list()
        prevStatus = False
        prevValue = initRange[0]-1
        prevAdded = False
        for v in range(initRange[0], initRange[-1]+2):
            currStatus = v in initRange
            if currStatus != prevStatus:
                if not prevAdded: geneRange.append((prevValue, prevStatus, \
                                  self.generateDesc(prevValue)))
                geneRange.append((v, currStatus, self.generateDesc(v)))
                prevAdded = True
            else:
                prevAdded = False
            prevStatus = currStatus
            prevValue = v
        return geneRange

    def formatInitRange(self, initRange):
        rangeList = None
        if type(initRange) is str: rangeList = eval(initRange)
        elif type(initRange) is list: rangeList = initRange
        else: rangeList = list()
        rangeList.sort()
        return rangeList

    def generateDesc(self, v):
        return '__INT_'+str(v)

    def __str__(self):
        return '==== FlatInt debug info ====\n' + \
               '= original range : ' + str(self.initRangeList) + '\n' + \
               '= generated list: ' + str(self.generatedList) + '\n'
