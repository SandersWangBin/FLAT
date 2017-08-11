#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class FlatStr:
    CHAR_SPECIAL = """!"#%&/()=?@${[]}+\^~*'-_:.;,צהו"""
    CHAR_LETTER = 'atoz'
    CHAR_NUMBER = '0369'

    def __init__(self, arg):
        self.initDefault, self.initRegex, self.initLength = arg
        self.formatInitValues()
        self.generatedList = self.generate()

    def formatInitValues(self):
        if self.initRegex == None:
            self.initRegex = '^'+self.initDefault+'$'
            self.initLength = [len(self.initdefault)]

    def generate(self):
        self.generatedList = list()
        self.generatedList.append((self.initDefault, True, \
                                   self.generateDesc(self.initDefault)))
        for v in self.convertCase(self.initDefault):
            m = True if re.search(self.initRegex, v) else False
            d = self.generateDesc(v)
            self.generatedList.append((v, m, d))

        self.addGeneratedList(self.CHAR_LETTER)
        self.addGeneratedList(self.CHAR_NUMBER)
        for c in self.CHAR_SPECIAL: self.addGeneratedList(c)
        return self.generatedList
        
    def addGeneratedList(self, c):
        for v in self.convertChar(self.initDefault, c):
            m = True if re.search(self.initRegex, v) else False
            d = self.generateDesc(v)
            self.generatedList.append((v, m, d))

    def convertCase(self, v):
        caseList = list()
        if v.islower(): caseList.append(v.upper())
        elif v.isupper(): caseList.append(v.lower())
        else:
            caseList.append(v.upper())
            caseList.append(v.lower())
        return caseList

    def convertChar(self, v, c):
        return [c+v, v+c]

    def generateDesc(self, v):
        return '__STR_'+str(v)

    def __str__(self):
        return '==== FlatStr debug info ====\n' + \
               '= original default: ' + str(self.initDefault) + '\n' + \
               '= original regex  : ' + str(self.initRegex) + '\n' + \
               '= original length : ' + str(self.initLength) + '\n' + \
               '= generated list  : ' + str(self.generatedList) + '\n'
