import random
a = [random.randint(1, 100) for i in range(100)]
print(a, set(a), sep='\n')
