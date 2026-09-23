import random
from random import shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""
for a in range(nr_letters):
    password += random.choice(letters) #Here it's picking a random letter from the list as many times the user has chose.
for b in range(nr_symbols):
    password += random.choice(symbols) #Here it's picking a random symbol from the list as many times the user has chose.
for c in range(nr_numbers):
    password += random.choice(numbers) #Here it's picking a random number from the list as many times the user has chose.
password1 = list(password) #I've created a list using list() but I could just use password1 = []
shuffle(password1)
# final_password = "".join(password1) - this way is simpler, but I needed to know how works .join I could have finished with a loop instead.
# print(f"Your password is: {final_password}")

password = "" #Here I'm saying that password is empty
for d in password1: #The do a loop where I will remove the letters, symbols and numbers from a list and print like a string
    password += d # here is part of the loop where I will add one by one from the list that I created "password1"

print(f"Your password is: {password}")
