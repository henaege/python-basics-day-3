# Use a built-in method to uppercase a string
name = "drew"
name_upper = name.upper()
print name_upper

# Loop through and uppercase
new_string = ""
for letter in name:
    new_string += letter.upper()
print new_string