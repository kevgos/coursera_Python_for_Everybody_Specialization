import sys
score = input('Please enter a score between 0.0 and 1.0: ')

try:
    score = float(score)
except:
    print('Please enter a numeric value')
    sys.exit()

if score < 0.0 or score > 1.0:
    print('Score is out of range')

def grader(grade):
    if score >= 0.9:
        output = 'A'
    elif score >= 0.8 and score < 0.9:
        output = 'B'
    elif score >= 0.7 and score < 0.8:
        output = 'C'
    elif score >= 0.6 and score < 0.7:
        output = 'D'
    elif score < 0.6:
        output = 'F'
    return output

toPrint = grader(score)
print(toPrint)
