# import string so we can use string.puncutation to get rid of punctuation

import string

counter = dict()

# open file and get rid of punctuation, make everything lower case and parse the words
# can use translate method, which is:  line.translate(str.maketrans(fromstr, tostr, deletestr))

with open('romeo-full.txt', 'r') as fhand:
    for line in fhand:
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
    # now we make a list of tuples using the dictionary and sort it
    lst = list()
    for key, val in list(counter.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    print(lst[:10])
