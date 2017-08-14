#!/usr/bin/env python

import os
from FlatExpCons import * 

from flat.lib.FlatInt import FlatInt
from flat.lib.FlatStr import FlatStr
from flat.lib.FlatList import FlatList

class FlatExp:
    @staticmethod
    def parser(ruleExp):
        ruleExpDoc = eval(ruleExp)
        if ruleExpDoc[EXP_TYPE] in EXP_TYPE_VALUES:
            return FlatExp.generateObj(ruleExpDoc, ruleExpDoc[EXP_TYPE])

    @staticmethod
    def generateObj(ruleExpDoc, ruleExpType):
        argTuple = tuple()
        for argName in EXP_RULE_VALUES[ruleExpType]:
            argValue = ruleExpDoc[EXP_RULE].get(argName, None)
            argTuple = argTuple + (argValue,)
        obj = eval(EXP_CLASS_VALUES[ruleExpType])
        return obj

    @staticmethod
    def generateOutput(geneList, geneElement):
        output = list()
        for t in geneList:
            value, matched, desc, default = t
            e = eval(geneElement)
            if e != None: output.append(e)
        return output
