# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.

import string

userfile = input('Please enter a .txt file: ')

counterDict = {}
delimiter = ''

with open(userfile, 'r') as fhand:
    for line in fhand:
        line = line.lower()
        line = line.rstrip()
        line = line.translate(str.maketrans('', '', string.punctuation))
        line = line.translate(str.maketrans('', '', string.digits))
        line = line.replace(" ", "")
        line = line.replace("\t", "")
        for char in line:
            if char not in counterDict:
                counterDict[char] = 1
            else:
                counterDict[char] += 1
counterList = []
for key, val in list(counterDict.items()):
    counterList.append((val,key))

counterListSorted = sorted(counterList)
print(counterListSorted)
        
        


