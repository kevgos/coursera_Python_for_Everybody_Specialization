count = 0
emptydict = {}

with open('words.txt', 'r') as fhand:
    for line in fhand:
        line = line.rsplit()
        for word in line:
            count = count + 1
            emptydict[word] = count

print(emptydict['our'])
print(emptydict)

# if wanted to get rid of duplicate words would do this:

count = 0
emptydict = {}

with open('words.txt', 'r') as fhand:
    for line in fhand:
        line = line.rsplit()
        for word in line:
            if word in emptydict:
                continue
            count = count + 1
            emptydict[word] = count

print(emptydict['our'])
print(emptydict)