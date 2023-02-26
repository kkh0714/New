numbers = [1,2,3,4,5,6,7,8,10,2,5,6,1,6,-1,34,6,8]

# MY OWN SOLUTION
largest_number = 0
current_number = 0
for i in numbers:
    current_number = i
    # print(current_number)
    if current_number > largest_number:
        largest_number = current_number
print(largest_number) 

# largest_number = numbers[0]
# for i in numbers:
#     if i > largest_number:
#         largest_number = i
# print(largest_number)