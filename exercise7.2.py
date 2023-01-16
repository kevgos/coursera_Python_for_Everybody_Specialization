filename = 'mbox-short.txt'

with open (filename, 'r') as fhand:
    accumulator = 0.0
    count = 0
    for line in fhand:
        line = line.rstrip()
        if line.find('X-DSPAM-Confidence:') == -1:
            continue
        accumulator = accumulator + float(line[19:])
        count = count + 1

average = accumulator/count
print(f'The average X-DSPAM-confidence is {average}')