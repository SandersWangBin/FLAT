#!/usr/bin/env python

class FlatList:
    def __init__(self, arg):
        self.initElement, = arg
        self.generatedElement = self.initElement

    def __str__(self):
        return '==== FlatList debug info ====\n' + \
               '= original element : ' + str(self.initElement) + '\n' + \
               '= generated element: ' + str(self.generatedElement) + '\n'
