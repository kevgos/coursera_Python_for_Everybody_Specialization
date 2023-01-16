day_dict = dict()
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From':
            continue
        if line[2] not in day_dict:
            day_dict[line[2]] = 1
        else:
            day_dict[line[2]] += 1
print(day_dict)
        
