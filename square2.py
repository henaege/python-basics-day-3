def print_star(num):
    print("* " * num)

columns = int(raw_input("How many columns? "))
rows = int(raw_input("How many rows? "))
while rows > 0:
    print_star(columns)
    rows -= 1