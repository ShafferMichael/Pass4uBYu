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
sort_keys = passwords_dict.items()
sorted_passwords_dict = sorted(sort_keys)
print(sorted_passwords_dict)


# passwords_list = passwordgenerator.generate_list(keyword, length)
print("debug-breakpoint")
