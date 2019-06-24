class Atom:
    def eval(self, arguments):
        if len(arguments) == 0:
            print("Error no arguments in atom")
        if len(arguments) == 1:
            return ["T"]
        else:
            return ["F"]


class Cdr:
    def eval(self, arguments):
        if len(arguments) == 0:
            print("Error no arguments in cdr")
            return None

        if len(arguments) == 1:
            return []
        else:
            return arguments[1:]


class Car:
    def eval(self, arguments):
        if len(arguments) == 0:
            print("Error no arguments in car")
            return None

        return [arguments[0]]