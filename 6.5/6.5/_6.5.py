# shift cipher

alpha = "abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift = 3):
  encrypted_str = ""
  for c in s:
    index = alpha.index(c)
    shifter_index = (index + shift) #% len(alpha)
    encrypted_str += alpha[shifter_index]
  return encrypted_str


def decrypt(e, shift = 3):
  decrypted_str = ""
  for c in e:
    index = alpha.index(c)
    shifter_index = (index - shift) #% len(alpha)
    decrypted_str += alpha[shifter_index]
  return decrypted_str

print(encrypt("helloworld"))
print(decrypt("khoorzruog"))
print(decrypt(encrypt("aaabbbcccddd")))