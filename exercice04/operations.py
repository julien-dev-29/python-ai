import sys

if len(sys.argv) < 3:
    print("Usage: python3 operations.py <number1> <number2>")
    print("Example:")
    print("    python3 operations.py 2 10")
    sys.exit()

if len(sys.argv) > 3:
    print("AssertionError: too many arguments")
    sys.exit()

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("AssertionError: only integer")
    sys.exit()

a = int(sys.argv[1])
b = int(sys.argv[2])

print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
if b == 0:
    print("Quotient: Error division by zero")
    print("Remainder: Error division by zero")
else:
    print(f"Quotient: {a / b}")
    print(f"Remainder: {a % b}")