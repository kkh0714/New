numbers = [1,2,4,1,5,7,5,1]

# MY OWN SOLUTION
# numbers.sort()
# current_number = numbers[0]
# for i in numbers:
#     # when i switch to a different or not the same number, it will not remove the i from the list
#     # e.g. [1,1,1,2,4,5,5,7] it will retain the last 1 when i == 2.
#     if i == current_number: 
#         numbers.remove(i)
#     current_number = i    
# print(numbers)

unique = []
for i in numbers:
    if i not in unique:
        unique.append(i)
print(unique)