#!/usr/bin/env python

class FlatList:
    def __init__(self, arg):
        self.initElement, = arg

    def __str__(self):
        return '==== FlatList debug info ====\n' + \
               '= original element: ' + str(self.initElement) + '\n'

