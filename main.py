
import passwordgenerator
# import UI
import priority_queue
import heapsort

# take in value
keyword = "Potato"
length = 8
passwords = {}

passwords = passwordgenerator.generate(keyword, length)
pqOrder = priority_queue.orderPasswordsPQ(passwords)
print("debug-breakpoint")
