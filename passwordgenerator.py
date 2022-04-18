import random

symbols = list("!@#$%^&*()1234567890_")
passwords = {}


def insert_str(keyword, str_to_insert, index):
    return keyword[:index] + str_to_insert + keyword[index:]


def rank_password(password, keyword):
    value = 0
    for char in password:
        if char in symbols:  # if special characters are in
            value += 2
        else:
            value += 1
        if password.count(char) > 1:  # if duplicate symbols present
            value -= 1
        if keyword in password:  # if the keyword is word for word in the password
            value = 0

    return value




def generate(keyword, length):
    spaces_to_fill = length - len(keyword)

    if len(keyword) >= length:
        return -1
    else:
        for x in range(100000):
            password = keyword
            for y in range(spaces_to_fill):
                random_int = random.randint(0, length - 1)
                random_char = random.choice(symbols)
                password = insert_str(password, random_char, random_int)

            rank = rank_password(password, keyword)
            passwords[password] = rank
        return passwords
