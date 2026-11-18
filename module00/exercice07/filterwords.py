import sys

def filter_words(words: list[str], n: int):
    return [word for word in words if len(word) >= n]

if len(sys.argv) != 3:
    print("Error")
    sys.exit()

argStr = sys.argv[1]
n = int(sys.argv[2])

words = argStr.split(" ")

words = filter_words(words, n)

print(f"{words}")