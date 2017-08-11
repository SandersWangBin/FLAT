#!/usr/bin/env python

import sys
sys.path.append('../src/')
from FlatObj import FlatObj

flatExp01 = """j'{"type":"int", "rule":{"range":[0,2,4,6]}}'.FLAT({"type":"list", "rule":{"element":"value if matched else None"}})"""
flatExp02 = """j'{"type":"int", "rule":{"range":"[12, 16] + range(0,10)"}}'.FLAT({"type":"list", "rule":{"element":"value if not matched else None"}})"""
flatExp03 = """j'{"type":"int", "rule":{"range":range(0,3) + range(4,7)}}'.FLAT({"type":"list", "rule":{"element":"(value, matched, desc)"}})"""
flatExp04 = """j'{"type":"str", "rule":{"default":"FlatTest01234", "regex":"^[a-zA-Z0-9_]+$", "length":"range(1,255)"}}'.FLAT({"type":"list", "rule":{"element":"(value,'POS' if matched else 'NEG')"}})"""

def verify(flatObj, expectedList):
    print 'FLAT EXP: ', flatObj.flatExp
    print 'FLAT OUT: ', str(flatObj.output)
    print 'Expected: ', str(expectedList)
    print ' => ', str(flatObj.output == expectedList)
    print

flatObj01 = FlatObj(flatExp01)
verify(flatObj01, [0, 2, 4, 6])

flatObj02 = FlatObj(flatExp02)
verify(flatObj02, [-1, 10, 11, 13, 15, 17])

flatObj03 = FlatObj(flatExp03)
verify(flatObj03, [(-1, False, '__INT_-1'), (0, True, '__INT_0'), (2, True, '__INT_2'), (3, False, '__INT_3'), (4, True, '__INT_4'), (6, True, '__INT_6'), (7, False, '__INT_7')])

flatObj04 = FlatObj(flatExp04)
verify(flatObj04, [('FlatTest01234', 'POS'), ('FLATTEST01234', 'POS'), ('flattest01234', 'POS'), ('atozFlatTest01234', 'POS'), ('FlatTest01234atoz', 'POS'), ('0369FlatTest01234', 'POS'), ('FlatTest012340369', 'POS'), ('!FlatTest01234', 'NEG'), ('FlatTest01234!', 'NEG'), ('"FlatTest01234', 'NEG'), ('FlatTest01234"', 'NEG'), ('#FlatTest01234', 'NEG'), ('FlatTest01234#', 'NEG'), ('%FlatTest01234', 'NEG'), ('FlatTest01234%', 'NEG'), ('&FlatTest01234', 'NEG'), ('FlatTest01234&', 'NEG'), ('/FlatTest01234', 'NEG'), ('FlatTest01234/', 'NEG'), ('(FlatTest01234', 'NEG'), ('FlatTest01234(', 'NEG'), (')FlatTest01234', 'NEG'), ('FlatTest01234)', 'NEG'), ('=FlatTest01234', 'NEG'), ('FlatTest01234=', 'NEG'), ('?FlatTest01234', 'NEG'), ('FlatTest01234?', 'NEG'), ('@FlatTest01234', 'NEG'), ('FlatTest01234@', 'NEG'), ('$FlatTest01234', 'NEG'), ('FlatTest01234$', 'NEG'), ('{FlatTest01234', 'NEG'), ('FlatTest01234{', 'NEG'), ('[FlatTest01234', 'NEG'), ('FlatTest01234[', 'NEG'), (']FlatTest01234', 'NEG'), ('FlatTest01234]', 'NEG'), ('}FlatTest01234', 'NEG'), ('FlatTest01234}', 'NEG'), ('+FlatTest01234', 'NEG'), ('FlatTest01234+', 'NEG'), ('\\FlatTest01234', 'NEG'), ('FlatTest01234\\', 'NEG'), ('^FlatTest01234', 'NEG'), ('FlatTest01234^', 'NEG'), ('~FlatTest01234', 'NEG'), ('FlatTest01234~', 'NEG'), ('*FlatTest01234', 'NEG'), ('FlatTest01234*', 'NEG'), ("'FlatTest01234", 'NEG'), ("FlatTest01234'", 'NEG'), ('-FlatTest01234', 'NEG'), ('FlatTest01234-', 'NEG'), ('_FlatTest01234', 'POS'), ('FlatTest01234_', 'POS'), (':FlatTest01234', 'NEG'), ('FlatTest01234:', 'NEG'), ('.FlatTest01234', 'NEG'), ('FlatTest01234.', 'NEG'), (';FlatTest01234', 'NEG'), ('FlatTest01234;', 'NEG'), (',FlatTest01234', 'NEG'), ('FlatTest01234,', 'NEG'), ('\xf6FlatTest01234', 'NEG'), ('FlatTest01234\xf6', 'NEG'), ('\xe4FlatTest01234', 'NEG'), ('FlatTest01234\xe4', 'NEG'), ('\xe5FlatTest01234', 'NEG'), ('FlatTest01234\xe5', 'NEG')])
