from LISP import LispMachine
import re


def main():
    print("Lisp repl")
    machine = LispMachine()

    inputPrompt = ""
    while inputPrompt != "(exit)":
        inputPrompt = input(">>")

        print("parsing:[" + inputPrompt + "]")
        output = machine.parseExpression(inputPrompt)
        print(str(output))


if __name__ == "__main__": main()
