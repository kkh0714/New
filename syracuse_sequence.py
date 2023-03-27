num = int(input("Please input a number: "))
length = 1

while num != 1:
    if num%2 == 0:
        num = num//2
    else:
        if num > 1:
            num = 3 * num + 1
    print("number:", num)
    length += 1
print(length)