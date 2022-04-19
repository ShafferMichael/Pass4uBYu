import passwordgenerator
import priority_queue
import heapsort
# import UI

# take in value
keyword = "Olivia"
length = 11


passwords_dict = passwordgenerator.generate_dict(keyword, length)
arr_of_keys = list()
for i in passwords_dict.keys():
    arr_of_keys.append(i)

heapsort.heap_sort(arr_of_keys)

max_score_heapsort = arr_of_keys[len(arr_of_keys)-1]

priority_queue_keys = priority_queue.PriorityQueue()
for j in arr_of_keys:
    priority_queue_keys.insert(j)

if not(priority_queue_keys.is_empty()):
    max_score_priority_queue = priority_queue_keys.pop()



print("debug-breakpoint")
