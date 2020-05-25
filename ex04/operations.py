import sys


def printUsage():
    print("Usage: python operations.py <number1> <number2>")
    print("Example:")
    print("    python operations.py 10 3")


if (len(sys.argv) == 1):
    printUsage()
elif (len(sys.argv) == 3):
    try:
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
        print("Sum:\t\t", arg1 + arg2)
        print("Difference:\t", arg1 - arg2)
        print("Product:\t", arg1 * arg2)
        if (arg2):
            print("Quotient:\t", arg1 / arg2)
            print("Remainer:\t", arg1 % arg2)
        else:
            print("Quotient:\t ERROR (div by zero)")
            print("Remainer:\t ERROR (modulo by zero)")
    except ValueError:
        print("InputError: only numbers\n")
        printUsage()
elif (len(sys.argv) > 3):
    print("InputError: too many arguments\n")
    printUsage()
elif (len(sys.argv) < 3):
    print("InputError: not enough arguments\n")
    printUsage()
