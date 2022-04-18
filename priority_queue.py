from queue import PriorityQueue

q = PriorityQueue()


def order_passwords_PQ(passwords):
    for key, value in passwords.items():
        q.put(passwords[value], key)
