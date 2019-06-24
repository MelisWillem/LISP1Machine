import LISP
import re


class LispMachine:
    def __init__(self):
        self._expressions = \
            {
                "atom": LISP.Atom(),
                "cdr": LISP.Cdr(),
                "car": LISP.Car()
            }

    def getExpressionObject(self, key):
        return None

    def parseExpression(self, stringExpression):
        regex = r"\(.*\)"
        p = re.compile(regex)

        regexMatch = p.match(stringExpression)
        if (regexMatch != None):
            sExpression = regexMatch.group()
            argumentsExpression = (sExpression[1:(len(sExpression) - 1)]) \
                .split(" ")
            argumentsWithoutEmpty = filter(
                (lambda a: a != '')
                , argumentsExpression)

            key = argumentsWithoutEmpty[1]
            expressionObject = self.getExpressionObject(key)

            return expressionObject.eval()

        return None

def main():
    print("Lisp repl")
    machine = LispMachine()

    inputPrompt = ""
    while inputPrompt != "(exit)":
        inputPrompt = input(">>")

        print("parsing:[" + inputPrompt + "]")
        print(LispMachine.parseExpression(inputPrompt))


if __name__ == "__main__": main()
