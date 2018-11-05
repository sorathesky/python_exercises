
alpha1 = ["a", "f", "b", "e", "d"]
alpha2 = ["g", "i", "h"]
alpha3 = "jklmnopqrstuvwxyz"

# Sort lists
alpha1.sort()
alpha2.sort()
print(alpha1)
print(alpha2)


# Inserting elements
alpha1.insert(2, "c")
print(alpha1)
print(alpha2)

# List to strings
alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)
print(alpha1)
print(alpha2)

alphabet = alpha1 + alpha2 + alpha3
print(alphabet)
