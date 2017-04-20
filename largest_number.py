import random

given = []
count = 10

while count > 0:
    given.append(random.randint(1, 50))
    count -= 1

print(given)
print(max(given))

# largest = 0
# i = 0
# while i < len(given) + 1:
#     largest = given(i)
#     i += 1
#     if given(i) > largest:
#         largest = given(i)

# print(largest)
