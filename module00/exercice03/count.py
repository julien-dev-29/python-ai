import sys
import string
from collections import Counter

def text_analyzer(text: str):
    """Return statistics for *text*.

    Keys:
        printable   printable characters
        uppercase   uppercase letters
        lowercase   lowercase letters
        punctuation ASCII punctuation (you can extend it to Unicode)
        space       whitespace characters (spaces, tabs, newlines, …)
    """
    try:
        counts = Counter()
        for c in text:
            if c.isprintable():
                counts["printable"] += 1
            if c.isupper():
                counts["uppercase"] += 1
            if c.islower():
                counts["lower"] += 1
            if c in string.punctuation:
                counts["punctuation"] += 1
            if c.isspace():
                counts["space"] += 1
        print(f"The text contains {counts[""]} printable character(s):")
        print(f"{counts["uppercase"]} upper letter(s)")
        print(f"{counts["lower"]} lower letter(s)")
        print(f"{counts["punctuation"]} punctuation marks(s)")
        print(f"{counts["space"]} space(s)")
    except TypeError:
        print("TypeError: argument is not a string")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Error: too many arguments")
    elif len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print("Error: provide an argument")