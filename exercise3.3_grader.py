# Write a program to prompt for a score between 0.0 and 1.0. If the 
# score is out of range, print an error message. If the score is between
#  0.0 and 1.0, print a grade using the following table: 
# >= 0.9 A   >= 0.8     B >= 0.7    C>= 0.6  D<0.6 F

import sys
score = input('Please enter a score between 0.0 and 1.0: ')

try:
    score = float(score)
except:
    print('Please enter a numeric value')
    sys.exit()


if score < 0.0 or score > 1.0:
    print('Score is out of range')
    
else:
    if score >= 0.9:
        print('A')
    elif score >= 0.8 and score < 0.9:
        print('B')
    elif score >= 0.7 and score < 0.8:
        print('C')
    elif score >= 0.6 and score < 0.7:
        print('D')
    elif score < 0.6:
        print('F')
    
    


