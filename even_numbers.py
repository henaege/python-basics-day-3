import random

given = []
count = 10

while count > 0:
    given.append(random.randint(1, 50))
    count -= 1

print(given)

for i in given:
        if i % 2 == 0:
            print i
