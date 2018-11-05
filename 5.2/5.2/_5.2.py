index = 0 
names = ["Josh", "Harry", "Leah", "Micah"]

while index < len(names):
    name = names[index]
    index = index + 1


# 1 - 10
total = 0
v = 1
while v <= 10:
    total = total + 1
    v = v + 1
print(total)

while True:
  a, b = int(input("a: ")), int(input("b: "))
  if a + b == 20:
    print("Stopping Loop")
    break
  else:
      print("Please make sure a + b = 20")

