# Function calling itself
# Recursion call stack
# Base case 

# Doubles the number n 
# double(2) -> 4
# double(15) -> 30
def double(n):
  if n == 0:
    return 0
 
  return double(n - 1) + 3

print(double(3))

def exponentiate(b, e):
  # Base case to end recursive loop
  if (e == 0): return 1
  # Recursive call
  return exponentiate(b, e-1) * b