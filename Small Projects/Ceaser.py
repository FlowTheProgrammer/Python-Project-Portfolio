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
            code_number = int(input("How many time would you like to shift the letters? 1-25: \n"))
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

    #Turns string into a list for easier indexing
    message = []
    newMessage = ''
    for i in message_to_encode:
        message.append(i)
    
    for i in message:
        if i.lower() in alphabet.keys():
            if alphabet[i.lower()] + code_number > 26:
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

    print("Your new message is!\n")
    print(newMessage)



    


user_input = ''

while True:

    user_input = input("Would you like to decode or encode a message?")

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


    
