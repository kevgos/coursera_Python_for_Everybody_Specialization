# want to find line 'New Revision: 39772' and extract the digits

import re
filename = input('Enter filename: ')
with open(filename, 'r') as fhand:
    mylist = []
    for line in fhand:
        x = re.findall('^New .*: ([0-9]+)', line)
        if len(x) > 0:
            for number in x:
                number = float(number)
            mylist.append(number)
list_sum = sum(mylist)
list_length = len(mylist)
average_num = int(list_sum/list_length)
print(f'{average_num}')
