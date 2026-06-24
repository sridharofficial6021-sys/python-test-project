

n = 7

a, b = 0, 1

for _ in range(n):
    a, b = b, a + b

print(a)

#  0, 1, 1, 2, 3, 5, 8, 13