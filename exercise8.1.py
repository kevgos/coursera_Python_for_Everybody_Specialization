# Write a function called chop that takes a list 
# and modifies it, removing the first and last elements, and returns None.

def chop(anyList):
    del anyList[0]
    del anyList[-1]
    print(anyList)

print(chop([1,2,3,4]))


# Then write a function called middle that takes a list and returns a 
# new list that contains all but the first and last elements.

def middle(anyList):
    return anyList[1:-1]

list = [1,2,3,4]
x = middle(list)
print(x)