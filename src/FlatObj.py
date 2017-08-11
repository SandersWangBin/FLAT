#!/usr/bin/env python

import re
from exp.FlatExp import *

class FlatObj:
    REG_FLAT_OBJ_EXP = r"j'(.*)'.FLAT\((.*)\)"

    def __init__(self, flatExp, objName=None):
        self.objName = objName
        self.flatExp = flatExp
        ruleExp, outExp = self.initFlatObj(flatExp)
        self.ruleObj = FlatExp.parser(ruleExp)
        self.outObj = FlatExp.parser(outExp)
        self.output = FlatExp.generateOutput(self.ruleObj.generatedList, \
                                             self.outObj.generatedElement)

    def initFlatObj(self, flatExp):
        match = re.search(self.REG_FLAT_OBJ_EXP, flatExp)
        if match:
            return match.group(1), match.group(2)
        else:
            raise Exception("ERROR: wrong FLAT expression")
            return None, None

    def __str__(self):
        returnStr = "==== FlatObj Debug Info ====\n" + \
            "= objName: " + str(self.objName) + "\n" + \
            "= FlatExp: " + str(self.flatExp) + "\n" + \
            "= output : " + str(self.output) + "\n"
        return returnStr
