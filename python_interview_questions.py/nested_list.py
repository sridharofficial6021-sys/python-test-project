data=[[1,2],[2,4],5]
out=[]
for item in data:
    if isinstance(item,list):
        out.extend(item)

    else:
        out.append(item)
print(out)            