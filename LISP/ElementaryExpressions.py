class Atom:
    def eval(self,arguments):
        if len(arguments) == 0:
            print("Error no arguments in atom")
        if len(self._arguments) == 1:
            return True
        else:
            return False


class Cdr:
    def eval(self,arguments):
        if len(arguments) == 0:
            print("Error no arguments in cdr")
            return None

        if len(self._arguments) == 1:
            return []
        else:
            return self._arguments[1:]


class Car:
    def eval(self,arguments):
        if len(arguments) == 0:
            print("Error no arguments in car")
            return None

        return self._arguments[0]