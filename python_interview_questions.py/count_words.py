s="hello hello world"
freq={}
for i in s.split():
    freq[i]=freq.get(i,0)+1
print(freq)
   