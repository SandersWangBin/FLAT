#!/usr/bin/env python

EXP_TYPE = 'type'
EXP_TYPE_INT = 'int'
EXP_TYPE_STR = 'str'
EXP_TYPE_BOOL = 'bool'
EXP_TYPE_ENUM = 'enum'
EXP_TYPE_LIST = 'list'

EXP_RULE = 'rule'
EXP_RULE_RANGE = 'range'
EXP_RULE_DEFAULT = 'default'
EXP_RULE_REGEX = 'regex'
EXP_RULE_LENGTH = 'length'
EXP_RULE_ELEMENT = 'element'

EXP_TYPE_VALUES = [EXP_TYPE_INT, \
                   EXP_TYPE_STR, \
                   EXP_TYPE_BOOL, \
                   EXP_TYPE_ENUM, \
                   EXP_TYPE_LIST]

EXP_RULE_VALUES = {EXP_TYPE_INT: \
                       [EXP_RULE_DEFAULT, \
                        EXP_RULE_RANGE], \
                    EXP_TYPE_STR: \
                       [EXP_RULE_DEFAULT, \
                        EXP_RULE_REGEX, \
                        EXP_RULE_LENGTH], \
                    EXP_TYPE_BOOL: [], \
                    EXP_TYPE_ENUM: \
                        [EXP_RULE_RANGE],
                    EXP_TYPE_LIST: \
                        [EXP_RULE_ELEMENT]}

EXP_CLASS_VALUES = {EXP_TYPE_INT:  'FlatInt(argTuple)',
                    EXP_TYPE_STR:  'FlatStr(argTuple)',
                    EXP_TYPE_BOOL: 'FlatBool(argTuple)',
                    EXP_TYPE_ENUM: 'FlatEnum(argTuple)',
                    EXP_TYPE_LIST: 'FlatList(argTuple)'}
