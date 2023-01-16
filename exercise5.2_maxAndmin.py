listnums = []

while True:
    userInput = input('Please enter a number: ')
    if userInput == 'done':
        break
        
    try:
        userInput = int(userInput)
    except:
        print('bad data')
        continue
    listnums.append(userInput)

print('The numbers input were: ', listnums)

def maximum(input):
    largest = None
    for elements in input:
        if largest is None or elements > largest:
            largest = elements
    return largest

def minimum(input):
    smallest = None
    for elements in input:
        if smallest is None or elements < smallest:
            smallest = elements
    return smallest

theLargest = maximum(listnums)
theSmallest = minimum(listnums)

print('The maximum number was: ', theLargest)
print('The smallest number was: ', theSmallest)



