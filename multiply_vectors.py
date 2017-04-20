import random

given1 = []
given2 = []
count = 10

while count > 0:
    given1.append(random.randint(-50, 50))
    given2.append(random.randint(-50, 50))
    count -= 1

print(given1)
print(given2)
prods = []

i = 0
while i < len(given1):
    prods.append(given1[i] * given2[i])
    i += 1
    
print(prods)