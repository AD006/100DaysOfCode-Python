alpha= "abcdefghijklmnopqrstuvwxyz"
alphabet=[]

for letter in alpha:
  alphabet.append(letter)

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

direction= input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text= input("Type your message:\n").lower()
shift= int(input("Type the shift number:\n"))

# Todo-1: Create a function called 'encrypt' that takes the 'orginal_text' and 'shift_amount' as inputs.
# Todo-2: Inside the 'encrypt' function, shift each letter of the 'orginal_text' forwards in the alphabet by the shift amount and print the encrypted text.
# Todo-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# Todo-4: What happens if you try to shift z?

# def encrypt(orginal_text, shift_amount):
#   cipher_text= ""
#   for letter in orginal_text:
#     shifted_postion= alphabet.index(letter) + shift_amount
#     shifted_postion %= len(alphabet)
#     cipher_text += alphabet[shifted_postion]

#   print(f"The encoded text is {cipher_text}")
  
# encrypt= encrypt(orginal_text= text, shift_amount= shift)

# Todo-5: Create a different function called 'decrypt' that takes the 'orginal_text' and 'shift_amount'
# Todo-6: Inside the 'decrypt' function, shift each letter of the 'orginal_text' backwards in the alphabet by the shift amount and print the decrypted text.
# Todo-7: Call the decrypt function and pass in the user inputs. You should be able to test the code and decrypt
# Todo-8: Combine the encrypt() and decrypt() functions into a single function called 'caesar'.

# def decrypt(orginal_text, shift_amount):
#   output_text= ""
#   for letter in orginal_text:
#     shifted_postion= alphabet.index(letter) - shift_amount
#     shifted_postion %= len(alphabet)
#     output_text += alphabet[shifted_postion]

#   print(f"The encoded text is {output_text}")

# decrypt= decrypt(orginal_text= text, shift_amount= shift)

def caesar(orginal_text, shift_amount, encode_or_decode):
  output_text= ""
  if direction == "decode":
    shift_amount *= -1
  for letter in orginal_text:
    if letter not in alphabet:
      output_text += letter
    else:
      shifted_postion= alphabet.index(letter) + shift_amount
      shifted_postion %= len(alphabet)
      output_text += alphabet[shifted_postion]

  print(f"The {encode_or_decode}d text is {output_text}")

caesar(orginal_text= text, shift_amount= shift, encode_or_decode= direction)

