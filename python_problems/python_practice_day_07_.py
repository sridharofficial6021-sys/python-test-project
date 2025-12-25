a=int(input())
b=int(input())
for i in range (8+1,15):
    print(i)


for i in range (1,11):
    if(i%2==0):
        print("even")    

    else:
        print("odd")


count=0
for i in range (1,11):
    if(i%2==0):
        count=count+1
        print(count)   

e_count = 0
o_count = 0

for i in range(1, 11):
    if i % 2 == 0:
        e_count = e_count + 1   
    else:
        o_count = o_count + 1  

print("Even count:", e_count)
print("Odd count:", o_count)


count=0
for i in range (1,100):
    if(i%3==0 and i%5==0):
        count=count+1
        print(count)
