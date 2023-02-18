weight = input("Weight: ")
weight_unit = input("(L)bs or (K)g: ")
# Wrong method
# if weight_unit == "L" or "l":
if weight_unit.upper() == "L":
    weight = int(weight) / 2.205
    print(f"You are {weight} kilos")
elif weight_unit.upper() == "K":
    weight = int(weight) * 2.205
    print(f"You are {weight} pounds")
else:
    print("Please input k/K or L/l")