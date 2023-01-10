"""
Simple Caesar Cipher
Functions

Beginner Project: 
There are no try/except
Assume correct inputs

*This project was done after the original cipher*
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(var,shift_num,dir):
        new_text = ''
        for letter in var:
            if letter in alphabet:
                pos = alphabet.index(letter)
                if dir == "encode":
                    new_pos = pos + shift_num
                elif dir == "decode":
                    new_pos = pos - shift_num
                new_letter = alphabet[new_pos]
                new_text += new_letter
            else:
                new_text += letter
        if dir == "encode":
            print(f"The encoded message is {new_text}!")
        elif dir == "decode":
            print(f"The decoded message is {new_text}!")

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift % 26
    caesar(var=text,shift_num=shift,dir=direction)

    user_input = input("Do you want to go again? Yes or No.")

    if user_input == "Yes":
        pass
    else:
        print("Bye Bye!")
        break


    