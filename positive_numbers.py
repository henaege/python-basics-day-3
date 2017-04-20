import random

given = []
count = 10

while count > 0:
    given.append(random.randint(-25, 25))
    count -= 1

print(given)

for i in given:
        if i > 0:
            print i