import sys

if len(sys.argv) > 1:
    merged = " ".join(sys.argv[1:])
    result = merged[::-1].swapcase()
else:
    result = "You must provide an argument"

print(result)