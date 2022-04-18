class passwordGenerator:
    def __init__(self, passwords):
        self.passwords = passwords

    def __repr__(self):
        return self.passwords

    def generate(self, keyword, length):
        spaces_to_fill = length - len(keyword)
        if len(keyword) >= length:
            return -1
        else:
            for char in keyword:





