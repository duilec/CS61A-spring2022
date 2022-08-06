import timeit

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest

    def insert_at_start(self, value):
        original_first = self.first
        self.first = value
        self.rest = Link(original_first, self.rest)

# From https://www.gutenberg.org/files/2600/2600-0.txt
filename = "warandpeace.txt"
big_file = open(filename, encoding="utf8")
big_str = big_file.read()
# Make a big python list
big_list = big_str.split(" ")

# Make a big linked list
big_ll = Link(big_list[0])
word_num = 1
current_link = big_ll
while word_num < len(big_list):
   current_link.rest = Link(big_list[word_num])
   current_link = current_link.rest
   word_num += 1

# Time the Python list
time_taken = timeit.timeit(lambda: big_list.insert(0, "happy"), number=100000)
print('Time the Python list' + time_taken)

# Time the linked list
time_taken = timeit.timeit(lambda: big_ll.insert_at_start("happy"), number=100000)
print('Time the linked list' + time_taken)