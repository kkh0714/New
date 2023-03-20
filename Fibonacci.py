# while loop
# number = int(input("Input Number that is >=3: "))
# first = 1
# second = 2
# count = 3
# print(f'The Fiboncci sequence with {number}: {first}')
# print(f'The Fiboncci sequence with {number}: {second}')
# while count <= number:
#     fibon = first + second
#     first = second
#     second = fibon
#     print(f'The Fiboncci sequence with {number}: {fibon}')
#     count += 1

# for loop
number = int(input("Input Number that is >=3: "))
first = 1
second = 2
print(f'The Fiboncci sequence with {number}: {first}')
print(f'The Fiboncci sequence with {number}: {second}')
for i in range(3, number+1):
    fibon = first + second
    first = second
    second = fibon
    print(f'The Fiboncci sequence with {number}: {fibon}')