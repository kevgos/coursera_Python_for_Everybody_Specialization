myinput_file = input('Enter a file name: ')

def emailCounter(userFile):
    import re
    dictCounter = {}
    with open(userFile,'r') as fhand:
        for line in fhand:
            line = line.rstrip()
            x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
            if len(x) < 1: continue
            for item in x:
                if item not in dictCounter:
                 dictCounter[item] = 1
                else:
                 dictCounter[item] += 1
        lst = list()
        for key,val in list(dictCounter.items()):
            lst.append((val,key))
        lst.sort(reverse=True)
        print(f'The top 10 most recurring emails are: {lst[:10]}')
        
      

emailCounter(myinput_file)