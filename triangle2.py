def print_star():
    print((" " * (space_count / 2)) + "*" * star_count + (" " * (space_count / 2)))

total_width = int(raw_input("How tall should the triangle be? ")) * 2
star_count = 1
space_count = total_width - star_count
loop_count = 1
while loop_count <= total_width:
    if star_count % 2 == 1:
        print_star()
    star_count += 1
    space_count -= 1
    loop_count += 1