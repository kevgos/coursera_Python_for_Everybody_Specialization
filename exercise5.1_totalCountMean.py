total = 0
count = 0

while True:
    userInput = input('Please enter a number: ')
    if userInput == 'done':
        break
        
    try:
        userInput = float(userInput)
    except:
        print('bad data')
        continue
    total = total + userInput
    count = count + 1
    mean = total/count


print('Total is: ', total)
print('Count is: ', count)
print('Mean is: ', mean)

