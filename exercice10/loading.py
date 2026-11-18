import time

def progress(lst: list):
    total = len(lst)
    start = time.time()
    bar = list("                     ")
    for i, elem in enumerate(lst):
        elapsed = time.time() - start
        eta = elapsed / (i + 1) * (total - i - 1)
        purcentage = (elem * 100) / total
        bar[int(purcentage * 2 / 10)] = "="
        bar[int(purcentage * 2 / 10) + 1] = ">"
        print(f"\rETA: {eta:.2f}s [ {purcentage:.0f}%] [{"".join(bar)}] {elem} / {total} | elapsed time {elapsed:.2f}s", end="", flush=True)
        yield elem

listy = range(1000)
ret = 0
for elem in progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)