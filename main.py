from collections import defaultdict

import passwordgenerator
# import UI
import priority_queue
import heapsort

# take in value
keyword = "Olivia"
length = 11
passwords = defaultdict(list)

passwords = passwordgenerator.generate_dict(keyword, length)
sort_keys = passwords.items()
new_items = sorted(sort_keys)
print(new_items)

print("debug-breakpoint")
