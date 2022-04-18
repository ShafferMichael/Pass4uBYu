import random

symbols = list("!@#$%^&*()1234567890_")
passwords = {}


def insert_str(keyword, str_to_insert, index):
    return keyword[:index] + str_to_insert + keyword[index:]


def rank_password(password, length, keyword):
    spaces_to_fill = length - len(keyword)
    value = 0.0
    for char in password:
        if char in symbols:  # if special characters are in
            value += 2
        else:
            value += 1
        if password.count(char) > 1:  # if duplicate symbols present
            value -= 1
        if keyword in password:  # if the keyword is word for word in the password
            value = 0
            break
        if password.find(keyword[:2]) != -1:
            value -= 1
        else:
            value += 1
        if password.find(keyword[1:3]) != -1:
            value -= 1
        else:
            value += 1
    if keyword[0:1] != password[0:1]:
        value -= 10
    else:
        value += 10
    if keyword[len(keyword)-1:len(keyword)] != password[len(password)-1:len(password)]:
        value -= 10
    else:
        value += 10

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

            rank = rank_password(password, length, keyword)
            passwords[password] = rank
        return passwords
