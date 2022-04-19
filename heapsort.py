# https://www.geeksforgeeks.org/how-to-maintain-dictionary-in-a-heap-in-python/
import heapq as hq
import heapq

def with_heapq(the_dict):
    items = [(-value, key) for key, value in the_dict.items()]
    smallest = heapq.nsmallest(10, items)
    return [-value for value, key in smallest]
