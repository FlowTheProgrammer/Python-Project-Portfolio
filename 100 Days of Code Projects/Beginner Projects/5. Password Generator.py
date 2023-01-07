"""
Simple Password Generator
Lists/Random/Loops
Beginner Project: 
There are no try/except
Assume correct inputs
"""


import random

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = alphabet.split(" ")

numbers = "0 1 2 3 4 5 6 7 8 9"
numbers = numbers.split(" ")

symbols = "! # $ % & * ( ) +"
symbols = symbols.split(" ")



print("Welcome to the password generator!\n")

num_letter = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
strpassword = ''

for i in range(num_letter):
    password +=alphabet[random.randint(0,len(alphabet)-1)]


for i in range(num_numbers):
    password +=numbers[random.randint(0,len(numbers)-1)]

for i in range(num_symbols):
    password +=symbols[random.randint(0,len(symbols)-1)]

random.shuffle(password)

for i in password:
    strpassword = strpassword + i

print(strpassword)
