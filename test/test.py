#!/usr/bin/env python

import sys
sys.path.append('../src/')
from FlatObj import FlatObj

flatExp01 = """j'{"type":"int", "rule":{"range":[0,2,4,6]}}'.FLAT({"type":"list", "rule":{"element":"value if matched else None"}})"""
flatExp02 = """j'{"type":"int", "rule":{"range":"[12, 16] + range(0,10)"}}'.FLAT({"type":"list", "rule":{"element":"value if not matched else None"}})"""
flatExp03 = """j'{"type":"int", "rule":{"range":range(0,3) + range(4,7)}}'.FLAT({"type":"list", "rule":{"element":"(value, matched, desc)"}})"""
flatExp04 = """j'{"type":"str", "rule":{"regex":"[a-zA-Z0-9_]", "length":"range(1,255)"}}'.FLAT({"type":"list", "rule":{"element":"(value,'POS' if matched else 'NEG')"}})"""

flatObj01 = FlatObj(flatExp01)
print flatObj01

flatObj02 = FlatObj(flatExp02)
print flatObj02

flatObj03 = FlatObj(flatExp03)
print flatObj03
