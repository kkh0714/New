# print([:-1])
n = int(input("Please input a number: "))
k = int(input("please input an order: "))
i = 1
while i <= k:
    n = n//10
    i += 1
digit = int(n%10)
print(digit)

