a=[1,3,5]
b=[2,4,6]
i=0;j=0;
out=[]

while i<len(a) and j<len(b):
    if a[i]<b[j]:
        out.append(a[i]);
        i+=1

    else:
        out.append(b[j]);
        j+=1

out.extend(a[i:])
out.extend(b[j:])

print(out)        



        
 
