#!/usr/bin/env python

class FlatRuleExp(object):
    REXP_TYPE = 'type'
    REXP_TYPE_INT = 'int'
    REXP_TYPE_STR = 'str'
    REXP_TYPE_BOOL = 'bool'
    REXP_TYPE_ENUM = 'enum'

    REXP_RULE = 'rule'
    REXP_RULE_RANGE = 'range'
    REXP_RULE_DEFAULT = 'default'
    REXP_RULE_REGEX = 'regex'
    REXP_RULE_LENGTH = 'length'

    @staticmethod
    def parser(ruleExp):
        REXP_TYPE_VALUES = [FlatRuleExp.REXP_TYPE_INT, \
                            FlatRuleExp.REXP_TYPE_STR, \
                            FlatRuleExp.REXP_TYPE_BOOL, \
                            FlatRuleExp.REXP_TYPE_ENUM ]

        ruleExpDoc = eval(ruleExp)
        if ruleExpDoc[FlatRuleExp.REXP_TYPE] in REXP_TYPE_VALUES:
            return FlatRuleExp.generateArg(ruleExpDoc, ruleExpDoc[FlatRuleExp.REXP_TYPE])

    @staticmethod
    def generateArg(ruleExpDoc, ruleExpType):
        REXP_RULE_VALUES = {FlatRuleExp.REXP_TYPE_INT: \
                               (FlatRuleExp.REXP_RULE_RANGE,), \
                            FlatRuleExp.REXP_TYPE_STR: \
                                (FlatRuleExp.REXP_RULE_DEFAULT, \
                                 FlatRuleExp.REXP_RULE_REGEX, \
                                 FlatRuleExp.REXP_RULE_LENGTH), \
                            FlatRuleExp.REXP_TYPE_BOOL: (), \
                            FlatRuleExp.REXP_TYPE_ENUM: \
                                (FlatRuleExp.REXP_RULE_RANGE,)}

        argTuple = tuple()
        for i in range(len(REXP_RULE_VALUES[ruleExpType])):
            argName = REXP_RULE_VALUES[ruleExpType][i]
            argValue = ruleExpDoc[FlatRuleExp.REXP_RULE].get(argName, None)
            argTuple = argTuple + (argValue,)
        return argTuple
