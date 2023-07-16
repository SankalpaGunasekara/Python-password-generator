import random
import string


def letter_generator(len):
    letter_list = []
    i = 0

    while i < len:
        random_num = random.randint(32, 127)
        ascii_char = chr(random_num)
        if ascii_char in string.ascii_letters:
            letter_list.append(ascii_char)
            i += 1
        else:
            continue
    return letter_list


def symbol_generator(len):
    symbol_list = []
    i = 0
    while i < len:
        random_num = random.randint(32, 127)
        ascii_char = chr(random_num)

        if ascii_char in string.punctuation:
            symbol_list.append(ascii_char)
            i += 1
        else:
            continue
    return symbol_list


def number_generator(len):
    symbol_list = []
    i = 0
    while i < len:
        random_num = random.randint(32, 127)
        ascii_char = chr(random_num)

        if ascii_char in string.digits:
            symbol_list.append(ascii_char)
            i += 1
        else:
            continue
    return symbol_list


# combination = []
pwd_length = 0
print("Welcome to 🐍Password Generator")

letters = int(input("How many letters would you like in your password = "))
symbols = int(input("How many symbols would you like in your password = "))
numbers = int(input("how many numbers would you like in your password = "))

raw_list = (
    letter_generator(letters) + symbol_generator(symbols) + number_generator(numbers)
)
# print(raw_list)

random.shuffle(raw_list)
password = "".join(raw_list)
print(f"\nYour password = {''.join(password)}\n")
