wordlist = []

with open('romeo.txt') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.split()
        for words in line:
            if wordlist.count(words) == 0:
                wordlist.append(words)

print(wordlist)
wordlist.sort()
print(wordlist)

# can use count function check if a string has an occurrence in a list yet
        