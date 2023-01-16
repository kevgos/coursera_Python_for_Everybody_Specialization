# Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the num-
# ber of messages from each person using a dictionary. After all the data has been read, print the person with the least 
# commits by creating a list of (count, email) tuples from the dictionary. 
# Then sort the list in reverse order and print out the person who has the most commits.

email_dict = {}
with open('mbox-short.txt','r') as fhand:
    for line in fhand:
        line = line.rsplit()
        if len(line) < 2 or line[0] != 'From:':
            continue
        email = line[1]
        if email not in email_dict:
            email_dict[email] = 1
        else:
            email_dict[email] += 1
#print(email_dict)

mail_sorter = list()
for key,val in list(email_dict.items()):
    mail_sorter.append((val,key))
mail_sorter_lowest = sorted(mail_sorter)
mail_sorter_highest = sorted(mail_sorter, reverse=True)

print(f'The lowest amount of commits is {mail_sorter_lowest[0]}')
print(f'The highest amount of commits is {mail_sorter_highest[0]}')
