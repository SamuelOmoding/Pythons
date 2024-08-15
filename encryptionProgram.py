# Encryption Program

import random
import string

# Create a string containing a space, all punctuation marks, digits (twice for extra randomness), and all letters (uppercase and lowercase)
chars = " " + string.punctuation + string.digits + string.digits + string.ascii_letters
# Convert strings to list characters
chars = list(chars)
# Make a copy of the list of characters
key = chars.copy()

# Randomly shuffle the 'key' list to create a unique mapping of original characters to encrypted characters
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt:")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
    
print(f"original message: {plain_text}") 
print(f"encrypted message: {cipher_text}") 

#DECRYPT
cipher_text = input("Enter a message to decrypt:")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")         
print(f"original message: {plain_text}") 
