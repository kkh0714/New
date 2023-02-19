numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    # This line reset the output variable with an empty string
    output = ""
    for count in range(x_count):
        output += "x"
    print(output)