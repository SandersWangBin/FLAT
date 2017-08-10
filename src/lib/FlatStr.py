#!/usr/bin/env python

class FlatStr:
    def __init__(self, arg):
        self.initDefault, self.initRegex, self.initLength = arg

    def __str__(self):
        return '==== FlatStr debug info ====\n' + \
               '= original default: ' + str(self.initDefault) + '\n' + \
               '= original regex  : ' + str(self.initRegex) + '\n' + \
               '= original length : ' + str(self.initLength) + '\n'

