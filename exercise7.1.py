filename = input('Please enter the filename: ')

with open (filename, 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        if line.find('X-DSPAM') == -1:
            continue
        print(line)