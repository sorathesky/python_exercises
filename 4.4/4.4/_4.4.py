# or, and, not
# Logical statements 
T = True
F = False

statement1 = 3 > 4 # False
statement2 = 10 % 5 == 0 # True
statement3 = "A".lower() == "a" # True
print(statement1, statement2, statement3)
print()

# If statements with and, or and not conjunctions\
# or
if F or F: print("F or F")
if F or T: print("F or T")
if T or F: print("T or F")
if T or T: print("T or T")
print("")

# and
if F and F: print("F and F")
if F and T: print("F and T")
if T and F: print("T and F")
if T and T: print("T and T")
print("")

# not
# not(3 == 6) 3 != 6
if not F: print("not F")
if not T: print("not T")



# Similarity between embedded if statements and 'and' conjunctions
