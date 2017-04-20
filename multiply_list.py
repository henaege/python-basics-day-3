import random

given = []
count = 10

while count > 0:
    given.append(random.randint(-50, 50))
    count -= 1

print(given)
prods = []
factor = random.randint(1, 50)
print(factor)
for i in given:
    prods.append(i * factor)

print(prods)