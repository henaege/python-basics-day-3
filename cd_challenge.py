fullName = "Drew Tolliver"
age = 35

myArray = []
myArray.append(fullName)
myArray.append(age)
print(myArray)

def say_hello():
    print("Hello!")

say_hello()

split_name = fullName.split(" ")
print(split_name)

def say_name():
    print("Hello " + split_name[0])

say_name()

def my_age(year):
    print(2017 - year)

my_age(1991)

def sum_odd_numbers():
    sum = 0
    for i in range(1, 5001, 2):
        sum += i
    return sum

print(sum_odd_numbers())