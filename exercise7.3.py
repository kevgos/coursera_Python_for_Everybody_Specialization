filename = input('Please enter a file name: ')
if filename == 'na na':
    print('NO')
    exit()
try:
    with open (filename, 'r') as fhand:
        accumulator = 0.0
        count = 0
        for line in fhand:
            line = line.rstrip()
            if line.find('X-DSPAM-Confidence:') == -1:
                continue
            accumulator = accumulator + float(line[19:])
            count = count + 1
except:
    print('please enter a valid filename.')
    exit()

average = accumulator/count
print(f'The average X-DSPAM-confidence is {average}')