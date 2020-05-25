import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----'}

if len(sys.argv) == 1:
    exit()

ok = 1
nb = 0
for x in sys.argv[1:]:
    list = []
    list = x.split()
    for w in list:
        if w.isalnum() is False:
            ok = 0
        nb += 1

final = []
n = 0
if ok == 1:
    for x in sys.argv[1:]:
        list = []
        list = x.split()
        for w in list:
            w = w.upper()
            for c in w:
                if c in MORSE_CODE_DICT:
                    final.append(MORSE_CODE_DICT[c])
                else:
                    print("ERROR")
                    sys.exit()
            n += 1
            if (n != nb):
                final.append("/")
    print(*final, sep=' ')
else:
    print("ERROR")
