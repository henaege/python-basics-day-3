def print_top(num):
    print("*" * num)

def print_bottom(num):
    print("*" * num)

def print_sides(num):
    print("*" + (" " * (num - 2)) + "*")

width = int(raw_input("How wide is the box? "))
height = int(raw_input("How high is the box? "))
print_top(width)
while (height - 2) > 0:
    print_sides(width)
    height -= 1

print_bottom(width)