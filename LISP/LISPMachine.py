import re
from LISP import Atom,Car,Cdr

class LispMachine:
    def __init__(self):
        self._expressions = \
            {
                "atom": Atom(),
                "cdr": Cdr(),
                "car": Car()
            }

    def getExpressionObject(self, key):
        return self._expressions.get(key)

    def parseExpression(self, stringExpression):
        regex = r"\(.*\)"
        p = re.compile(regex)

        regexMatch = p.match(stringExpression)
        if (regexMatch != None):
            sExpression = regexMatch.group()
            argumentsExpression = (sExpression[1:(len(sExpression) - 1)]) \
                .split(" ")
            argumentsWithoutEmpty = list(filter(
                (lambda a: a != '')
                , argumentsExpression))

            key = argumentsWithoutEmpty[0]
            expressionObject = self.getExpressionObject(key)

            return expressionObject.eval(argumentsWithoutEmpty[1:])

        return None
