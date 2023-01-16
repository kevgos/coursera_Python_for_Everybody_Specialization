email_dict = dict()
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From':
            continue
        if line[1] not in email_dict:
            email_dict[line[1]] = 1
        else:
            email_dict[line[1]] += 1
#print(email_dict)

# could also the get method takes a key and a default value as arguments
# If the key is found in the dictionary then get returns the corresponding value, otherwise it returns the default value

email_dict = dict()
with open('mbox-short.txt', 'r') as fhand:
    for line in fhand:
        line = line.rstrip()
        line = line.rsplit()
        if len(line) == 0 or line[0] != 'From':
            continue
        if line[1] not in email_dict:
            email_dict[line[1]] = 1
        else:
            email_dict[line[1]] = email_dict.get(line[1], 0) + 1
#print(email_dict)


# Want to count who has the maximum amount of emails in the dictionary
# could try make a list of all the (keys , values) in sublists. Then loop through the list using indexing and get the max.
# method items, which returns all items as a type that can be converted to a list
counter = 0
highestVal = []
mail_counts_list = list(email_dict.items())
for mailsubsets in mail_counts_list:
    if mailsubsets[1] > counter:
        counter = mailsubsets[1]
        highestVal = mailsubsets

#print(highestVal)

# Could also loop through the list in a different way, loop using sublist1,sublist2

biggest_count = 0
biggest_word = None

for name,value in mail_counts_list:
    if value > biggest_count:
        biggest_count = value
        biggest_word = name
print(biggest_word, biggest_count)

