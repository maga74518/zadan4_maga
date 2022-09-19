import random
b, a = [], [random.randint(1, 100) for i in range(15)]

for num in a:
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            b.append(num)
            break
print(a, b, sep='\n')