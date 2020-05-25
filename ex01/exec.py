import sys

if len(sys.argv) == 1:
    exit()
list = []
for value in sys.argv[1:]:
    value = ''.join(reversed(value))
    list.append(value.swapcase())

list.reverse()
print(*list)
