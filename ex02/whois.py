import sys

if (len(sys.argv) == 2):
    try:
        n = int(sys.argv[1])
        if (n == 0):
            print("I'm Zero.")
        elif n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except ValueError:
        print("ERROR")
elif len(sys.argv) != 1:
    print("ERROR")
