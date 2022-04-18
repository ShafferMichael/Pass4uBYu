import random

symbols = list("!@#$%^&*()1234567890_")


class passwordgenerator:
    def __init__(self, passwords):
        self.passwords = passwords

    def __repr__(self):
        return self.passwords

    def insert_str(self, keyword, str_to_insert, index):
        return keyword[:index] + str_to_insert + keyword[index:]

    def rank_password(self, password):
        value = 0
        for char in password:
            if char in symbols:
                value += 2
            else:
                value += 1
            if password.count(char) > 1:
                value -= 1
        return value

        # repeating duplicates


def generate(self, keyword, length):
    password = ''
    spaces_to_fill = length - len(keyword)

    if len(keyword) >= length:
        return -1
    else:
        for x in range(100000):
            for y in range(spaces_to_fill):
                random_int = random.randint(0, length - 1)
                random_char = random.choice(symbols)
                password = self.insert_str(keyword, random_char, random_int)

            rank = self.rank_password(password)
            self.passwords[password] = rank
        return self.passwords
