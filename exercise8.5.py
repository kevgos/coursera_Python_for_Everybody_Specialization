with open('mbox-short.txt', 'r') as fhand:
    count = 0
    for line in fhand:
        line = line.rstrip()
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From': continue
        print(line[1])
        count = count + 1

print(f'There were {count} lines read here.')




        