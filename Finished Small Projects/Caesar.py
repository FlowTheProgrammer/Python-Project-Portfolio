import os

#Dict of letters
alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
             'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 
             'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
keys = list(alphabet.keys())
vals = list(alphabet.values())




#Encoder
def encodeMessage():
    print("Welcome to the Encoder!")
    print("-----------------------\n")

    #Loops until user inputs a valid number
    message_to_encode = input("Enter the text you would like to encode:\n")
    while True:
        try: 
            code_number = int(input("How many times would you like to shift the letters? 1-25: \n"))
            while code_number < 1 or code_number > 25:
                while True:
                    try: 
                        print()
                        print("Enter a number from 1-25")
                        print()
                        code_number = int(input("How many times would you like to shift the letters? 1-25: \n"))
                        break
                    except ValueError:
                        print("Invalid Input: Please input a number")
                        print()
            break
        except ValueError:
            print("Invalid Input: Please input a number")
            print()
    print()

    while True:

        user_input = input("Would you like to encode the message to the left or the right?:\n")

        if user_input.lower() == "left":
            os.system('cls')
            messageLeft(message_to_encode,code_number,"encode")
            break
        elif user_input.lower() == "right":
            os.system('cls')
            messageRight(message_to_encode,code_number,"encode")
            break
        else:
            print("I don't understand your input, Try Again.\n")






def messageRight(messageEncode,code,method):
        #Turns string into a list for easier indexing
        message = []
        newMessage = ''
        for i in messageEncode:
            message.append(i)
        
        for i in message:
            if i.lower() in alphabet.keys():
                if alphabet[i.lower()] + code >= 26:
                    num = alphabet[i.lower()] + code - 26
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
                else:
                    num = alphabet[i.lower()] + code
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
            else:
                newMessage = newMessage + i
        if method == "encode":
            print("Your new message is!\n")
            print(newMessage)
        elif method == "decode":
            print("The decoded message is!\n")
            print(newMessage)





def messageLeft(messageEncode,code,method):
    #Turns string into a list for easier indexing
        message = []
        newMessage = ''
        for i in messageEncode:
            message.append(i)
        
        for i in message:
            if i.lower() in alphabet.keys():
                if alphabet[i.lower()] - code <= 0:
                    num = alphabet[i.lower()] - code + 26
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
                else:
                    num = alphabet[i.lower()] + code
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
            else:
                newMessage = newMessage + i
        if method == "encode":
            print("Your new message is!\n")
            print(newMessage)
        elif method == "decode":
            print("The decoded message is!\n")
            print(newMessage)


def chooseDecodeMessage():
    while True:

        user_input = input("Would you like to use a certain key or bruteforce? Type key or bruteforce: \n")

        if user_input.lower() == "key":
            os.system('cls')
            keyDecode()
            break
        elif user_input.lower() == "bruteforce":
            os.system('cls')
            bruteForceDecode()
            break
        else:
            print("I don't understand your input, Try Again.\n")




def keyDecode():
    print("Welcome to the Key Decoder!")
    print("--------------------------\n")

    #Loops until user inputs a valid number
    message_to_decode = input("Enter the text you would like to decode:\n")
    while True:
        try: 
            code_number = int(input("How many times would you like to shift the letters? 1-25: \n"))
            while code_number < 1 or code_number > 25:
                while True:
                    try: 
                        print()
                        print("Enter a number from 1-25")
                        print()
                        code_number = int(input("How many times would you like to shift the letters? 1-25: \n"))
                        break
                    except ValueError:
                        print("Invalid Input: Please input a number")
                        print()
            break
        except ValueError:
            print("Invalid Input: Please input a number")
            print()
    print()

    while True:

        user_input = input("Would you like to decode the message to the left or the right?:\n")

        if user_input.lower() == "left":
            os.system('cls')
            messageLeft(message_to_decode,code_number,"decode")
            break
        elif user_input.lower() == "right":
            os.system('cls')
            messageRight(message_to_decode,code_number,"decode")
            break
        else:
            print("I don't understand your input, Try Again.\n")




#Prints out every variation
def bruteForceDecode():
    listOfDecodes = []
    print("Welcome to the Bruteforce Decoder!")
    print("--------------------------\n")

    message_to_decode = input("Enter the text you would like to decode:\n")

    
    message = []
    newMessage = ''
    for i in message_to_decode:
        message.append(i)

    code_number = 1
    for i in range(25):
        for i in message:
            if i.lower() in alphabet.keys():
                if alphabet[i.lower()] + code_number >= 26:
                    num = alphabet[i.lower()] + code_number - 26
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
                else:
                    num = alphabet[i.lower()] + code_number
                    pos = vals.index(num)
                    key = keys[pos]
                    newMessage = newMessage + key
            else:
                newMessage = newMessage + i
        listOfDecodes.append(newMessage)
        newMessage = ''
        code_number += 1
    print("\nHere are all the possible variations of the message!:\n")
    for i in listOfDecodes:
        print(i)


#Init
user_input = ''

while True:

    user_input = input("Would you like to decode or encode a message?:\n")

    if user_input.lower() == "decode":
        os.system('cls')
        chooseDecodeMessage()
        break
    elif user_input.lower() == "encode":
        os.system('cls')
        encodeMessage()
        break
    else:
        print("I don't understand your input, Try Again.\n")


    
