import random
import string

class passwordGenerator:
    def __init__(self, passwords):
        self.passwords = passwords

    def __repr__(self):
        return self.passwords

    def insert_str(string, str_to_insert, index):
        return string[:index] + str_to_insert + string[index:]

    def generate(self, keyword, length):
        spaces_to_fill = length - len(keyword)
        symbols = list("!@#$%^&*()1234567890_-+=")
        if len(keyword) >= length:
            return -1
        else:
            for x in range(100000):
                for x in range(spaces_to_fill):
                    random_char = random.choice(symbols)






