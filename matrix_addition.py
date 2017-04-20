# import random

given1 = [[1, 3], [2, 4]]
given2 = [[5, 2], [1, 0]]
# count = 0

# # while count > 0:
# #     given.append(random.randint(-50, 50))
# #     count -= 1

# print(given1)
# print(given2)
# # while count < len(given1):
# sum = [[(given1[0][0] + given2[0][0])], [(given1[0][1] + given2[0][1])],
# [(given1[1][0] + given2[1][0])], [(given1[1][1] + given2[1][1])]]
#     # count += 1
# print(sum)
# factor = random.randint(1, 50)
# print(factor)
# for i in given:
#     prods.append(i * factor)

# print(prods)

sum = [[],[]]

for i in given1:
    sum.append(i)
    


def matrix_sum(list1, list2):
    sum = [[(list1[0][0] + list2[0][0]), (list1[0][1] + list2[0][1])],
    [(list1[1][0] + list2[1][0]), (list1[1][1] + list2[1][1])]]
    return sum

print(given1)
print(given2)
print(matrix_sum(given1, given2))