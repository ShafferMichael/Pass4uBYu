import passwordgenerator
import priority_queue
import heapsort
# import UI

# take in value
keyword = input("Enter a keyword you'd like your password based around: ")
inputVar = True
while inputVar:
    length = int(input("Enter a number greater than 12: "))
    if length >= 12:
        break
    else:
        print("Try again (enter a string for keyword and an integer greater than or equal to 12 for length.")




passwords_dict = passwordgenerator.generate_dict(keyword, length)
arr_of_keys = list()
for i in passwords_dict.keys():
    arr_of_keys.append(i)

heapsort.heap_sort(arr_of_keys)

max_score_heapsort = arr_of_keys[len(arr_of_keys) - 1]

priority_queue_keys = priority_queue.PriorityQueue()
for j in arr_of_keys:
    priority_queue_keys.insert(j)

if not (priority_queue_keys.is_empty()):
    max_score_priority_queue = priority_queue_keys.pop()

topPasswords = passwords_dict[max_score_heapsort][0: 30]


print(*topPasswords, sep = "\n")
# a = topPasswords
# s = '\n'.join([str(i) for i in a])  # pass the string instead of an array.
# UI.sg.Output("Synchronization completed", f"The following items have been added: \n", f"{s}")



