# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour 
# from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once
#  you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

timeCounterdict = {}
time = ''
with open('mbox-short.txt','r') as fhand:
    for line in fhand:
        line = line.rsplit()
        if len(line) < 2 or line[0] != 'From':
            continue
        time = line[5]
        time = time[0:2]
        if time not in timeCounterdict:
            timeCounterdict[time] = 1
        else:
            timeCounterdict[time] += 1

timeList = []
for key, val in list(timeCounterdict.items()):
    timeList.append((key, val))
timeList.sort()
for val,count in timeList:
    print(val, count)
        