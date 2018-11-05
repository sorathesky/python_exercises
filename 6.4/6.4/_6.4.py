# Return function

# => "123" -> "321"
# Reverse a string

def reverse(s):
  new_str = ""
  for i in range(len(s)):
    new_str += s[len(s) - i -1]
  return new_str

print(reverse("123"))
print(reverse("abc"))


# Void function
# A palindrome a reversable string that runs the same forwards and backwards

def is_palindrome(p):
  for i in range(len(p)//2):
    if p[i] != p[len(p) - i - 1 ]:
      print("No this is a palindrome")
      return
  print("Yes this is a palindrome")

is_palindrome("1221")
is_palindrome("abba")

