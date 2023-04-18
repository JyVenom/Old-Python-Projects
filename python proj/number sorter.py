import random
number0 =7#random.randint(1,100)
number1 = 58#random.randint(1,100)
number2 =  91#random.randint(1,100)
number3 = 13#random.randint(1,100)
number4 = 90#random.randint(1,100)
number5 = 62#random.randint(1,100)
number6 = 52#random.randint(1,100)
number7 = 58#random.randint(1,100)
number8 = 41#random.randint(1,100)
number9 = 40#random.randint(1,100)
numbers=[number0,number1,number2,number3,number4,number5,number6,number7,number8,number9]
print("the random numbers are:")
print(number0)
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)
print(number6)
print(number7)
print(number8)
print(number9)
print("the sorted in desending order numbers are:")
z=10
for y in range(0, 10):
    r=0
    #print('y=',y)#yifeng
    max0=numbers[0]
    for x in range(0, z):
        #print('x=',x)#yifeng
       # print('z=',z)#yifeng
        if max0 < numbers[x]:
            max0 = numbers[x]
            max1=x
        if x > 0:
            if max0 == numbers[x]:
                print(numbers[x])
                r=1
    numbers.remove(numbers[max1])
    z = z-1
    if r==0:
        print(max0)
