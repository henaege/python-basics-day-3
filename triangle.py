def print_star():
    print((" " * (space_count / 2)) + "*" * star_count + (" " * (space_count / 2)))

total_width = 10
star_count = 1
space_count = total_width - star_count
loop_count = 1
while loop_count <= 10:
    if star_count % 2 == 1:
        print_star()
    star_count += 1
    space_count -= 1
    loop_count += 1