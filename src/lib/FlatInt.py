#!/usr/bin/env python

class FlatInt:
    def __init__(self, arg):
        self.initRange, = arg

    def __str__(self):
        return '==== FlatInt debug info ====\n' + \
               '= original range: ' + str(self.initRange) + '\n'
