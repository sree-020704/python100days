import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '(', ')']

print("Welcome to the Python password generator!")

nr_letters = int(input("How many letters would you like in your password?:\n"))
nr_symbols = int(input("How many symbols would you like?:\n"))
nr_numbers = int(input("How many numbers would you like?:\n"))

# Initialize password_list as a list (not a string)
password_list = []

# Add random letters, symbols, and numbers to the password list
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the password list to ensure it's randomly ordered
random.shuffle(password_list)

# Join the list to form a string
password = ''.join(password_list)
print("Your generated password is:", password_list)
print("Your generated password is:", password)

