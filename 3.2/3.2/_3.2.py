
#appending to lists
alpha = ["a", "b", "c", "d"]
alpha.append("e")
alpha = alpha + ["f"]
print(alpha)
print()

# remove from alpha by indexing 
d_index = alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)

# remove method to remove index
alpha.remove("c")
print(alpha)