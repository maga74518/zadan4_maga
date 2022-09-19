# 30. Вычислить число заданной точностью d

import random

a = str(random.uniform(0.1, 100))
print(a)

b = input()
c = len(b[b.find('.'):])-1

if len(b[b.find('.')::]) > len(a[a.find('.')::]):
    a = str(a) + '0' * (len(b) - len(str(a)))
elif len(b[b.find('.')::]) < len(a[a.find('.')::]):
    a = a[:a.find('.')] + a[a.find('.'):c+3]
print(a)