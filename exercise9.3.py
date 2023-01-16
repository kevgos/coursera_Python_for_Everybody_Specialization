email_dict = dict()
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From':
            continue
        if line[1] not in email_dict:
            email_dict[line[1]] = 1
        else:
            email_dict[line[1]] += 1
print(email_dict)