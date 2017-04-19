num1 = int(raw_input("Choose first number: "))
num2 = int(raw_input("Choose second number: "))
print("Start from: %d") % (num1)
print("End on: %d") % (num2)
for i in range(num1, num2 + 1):
    print i