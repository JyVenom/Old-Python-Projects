x=0
y=0
z=1
mylist=[1]*1000
x=0
for y in range(2,1001):
    for x in range(z,1000,y):
        if (mylist[x] is 1):
            mylist[x]=mylist[x]^1
        elif (mylist[x] is 0):
            mylist[x]=mylist[x]^1
    x=0
    z+=1
print(mylist)
