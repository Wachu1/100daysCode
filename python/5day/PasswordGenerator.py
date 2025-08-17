import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your passowrd? \n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(password)













# POPRAWNE
# passwrod = ""
#
# for char in range(1, nr_letters + 1):
#
#     random_char = random.choice(letters)
#     passwrod += random_char
#
# for char in range(1, nr_symbols + 1):
#
#     random_char = random.choice(symbols)
#     passwrod += random_char
#
# for char in range(1, nr_numbers + 1):
#
#     random_char = random.choice(numbers)
#     passwrod += random_char
#
#
# print(passwrod)









#
# sum = nr_letters + nr_numbers + nr_symbols
#
# new_letters = []
# new_symbols = []
# new_numbers = []
#
# los = [letters, numbers, symbols]
# for password in los:
#
#     for letter in range(nr_letters):
#         new_letters += letter
#
#     for symb in range(nr_symbols):
#         new_symbols += symb
#
#     for num in range(nr_numbers):
#         new_numbers += num
#
# print(new_letters, new_symbols, new_numbers)