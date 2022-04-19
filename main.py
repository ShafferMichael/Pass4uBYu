from collections import defaultdict

import passwordgenerator
# import UI
import priority_queue
import heapsort

# take in value
keyword = "Olivia"
length = 11
passwords_dict = defaultdict(list)

passwords_dict = passwordgenerator.generate_dict(keyword, length)
arr_of_keys = list()
for i in passwords_dict.keys():
    arr_of_keys.append(i)

heapsort.heapSort(arr_of_keys)

priority_queue_keys = priority_queue.PriorityQueue()
for j in arr_of_keys:
        priority_queue_keys.insert(j)





print("debug-breakpoint")
