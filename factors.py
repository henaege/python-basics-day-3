num = int(raw_input("Please provide a number to factor: "))

for i in range(1, num + 1):
    if num % i == 0:
        print i