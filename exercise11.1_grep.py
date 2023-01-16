import re

userinput = input('Enter a regular expression:')
with open('mbox.txt', 'r') as fhand:
    counter = 0
    for line in fhand:
        if re.search(userinput, line):
            counter += 1
print(f'There are {counter} lines that match {userinput}')
