def print_top(num):
    print("*" * num)

def print_bottom(num):
    print("*" * num)

def print_middle(message):
    print("*" + " " + message + " " + "*")

text = raw_input("What will the banner say? ")
width = len(text) + 4
# height = int(raw_input("How high is the box? "))
print_top(width)
print_middle(text)

print_bottom(width)