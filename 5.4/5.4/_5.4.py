alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
my_string = "Packt publishing rocks!"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Prog 1 
total = 0
for n in numbers:
  if n % 2 == 0:
   total += n 
print(total)

# Prog 2
characters = []
for ch in my_string:
  if ch not in vowels and ch in alpha:
   characters.append(ch)
consonants = ''.join(characters)
print(consonants)

# Extract consonants from a string
