# firstname, M., lastname

first_name = str(input("Please enter your name: "))
middle_name = str(input("Please enter your middle initial: "))
last_name = str(input("Please enter your last: "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s} {last}"
print(name_format.format(first = first_name, middle = middle_name, last = last_name))