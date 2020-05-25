import sys
import string

arr = []

if (len(sys.argv) == 3):
    try:
        s = sys.argv[1]
        if s.isdigit() is True:
            print("ERROR")
        else:
            n = int(sys.argv[2])
            for i in string.punctuation:
                s = s.replace(i, '')
            arr = s.split(" ")
            arr2 = []
            for i in arr:
                if len(i) > n:
                    arr2.append(i)
            print(arr2)
    except ValueError:
        print("ERROR")
else:
    print("ERROR")
