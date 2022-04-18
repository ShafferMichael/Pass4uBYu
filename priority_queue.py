from queue import PriorityQueue

q = PriorityQueue()

def orderPasswordsPQ(passwords):
    for x in passwords:
        q.put(passwords)
