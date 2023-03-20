# while loop
# number = int(input("Number: "))
# start = 1
# factor = 1
# while start <= number:
#     factor = factor * start
#     start += 1
# print(f"The factorial of {number} is: " + str(factor))

# for loop
number = int(input("Number: "))
factorial = 1
for factor in range(1, number+1):
    factorial = factorial * factor
print(f"The factorial of {number} is: " + str(factorial))