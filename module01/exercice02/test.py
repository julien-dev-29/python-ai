from vector import Vector

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)

v2 = v1 / 2.0
print(v2)

v1 / 0

2.0 / v1

v3 = v1 + v2

print(v3)