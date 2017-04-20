name = "Hootie and the Blowfish"
new_name = name[::-1]
print new_name

characters_from_string = []
for character in name:
    characters_from_string.append(character)
characters_from_string.reverse()
print("".join(characters_from_string))