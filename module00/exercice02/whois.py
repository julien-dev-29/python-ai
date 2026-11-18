import sys
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        if num == 0:
            result = "I'm Zero"
        elif num % 2 == 0:
            result = "I'm Even"
        else:
            result = "I'm Odd"
    except ValueError:
        result = "AssertionError: argument is not an integer"
else:
    result = "AssertionError: no argument provided"
print(result)