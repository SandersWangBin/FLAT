#!/usr/bin/env python

import sys
sys.path.append('../src/')
from FlatObj import FlatObj

flatExp01 = """j'{"type":"int", "rule":{"range":[0,2,4,6]}}'.FLAT({"out":"list", "format":"value if matched else None"})"""
flatExp02 = """j'{"type":"str", "rule":{"regex":"[a-zA-Z0-9_]", "length":"range(1,255)"}}'.FLAT({"out":"list", "format":"(value,'POS' if matched else 'NEG')"})"""

flatObj01 = FlatObj(flatExp01)
flatObj02 = FlatObj(flatExp02)
