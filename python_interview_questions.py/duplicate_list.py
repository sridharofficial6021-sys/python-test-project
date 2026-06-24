

lst = [1,2,2,3,1,4]

seen = set()

res = []

for x in lst:
    if x not in seen:
        seen.add(x)
        res.append(x)

print(res)



