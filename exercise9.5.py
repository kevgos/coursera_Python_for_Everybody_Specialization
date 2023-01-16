# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.

index = 0
mydict = {}
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand: 
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From:':
            continue
        for word in line:
            if word == 'From:':
                continue
            index = word.find('@') + 1
            if word[index:] not in mydict:
                mydict[word[index:]] = 1
            else:
                mydict[word[index:]] += 1
#print(mydict)


# could also index the second word in line 33 here, which is the mail address
email = ''
index = 0
mydict = {}
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From:':
            continue
        email = line[1]
        index = email.find('@') + 1
        if email[index:] not in mydict:
            mydict[email[index:]] = 1
        else:
            mydict[email[index:]] += 1
print(mydict)
