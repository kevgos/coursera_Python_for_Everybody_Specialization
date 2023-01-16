number_list = []

while True:
    number_input = input('enter a number, to stop enter done: ')
    if number_input == 'done': break
    number_addtolist = float(number_input)
    number_list.append(number_addtolist)

maxi_num = max(number_list)
mini_num = min(number_list)
print(f'The list is {number_list}')
print(f'The max number is {maxi_num} and the minimum number is {mini_num}')







        