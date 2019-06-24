import unittest
import LISP


class TestLisMachine(unittest.TestCase):
    def _runSingleExpression(self, expression, expectedResult):
        machine = LISP.LispMachine()
        result = machine.parseExpression(expression)

        self.assertEqual(expectedResult, result)

    def testCar(self):
        self._runSingleExpression("(car (1 2))", ["1"])

    def testCdr(self):
        self._runSingleExpression("(cdr (1 2))", ["2"])

    def testAtom(self):
        self._runSingleExpression("(atom (1 2))", ["F"])
        self._runSingleExpression("(atom (1) )", ["T"])

if __name__ == '__main__':
    unittest.main()
