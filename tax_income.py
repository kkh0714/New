income = int(input('enter income: ')) 
tax = 0
if income >=0 and income <= 18200:
    tax = 0
if income >= 18201:
    if income <= 45000:
        tax = tax + (income - 18200) * 0.19
    else:
        tax = tax + (45000 - 18200) * 0.19
print(tax)
if income >= 45001:
    if income <= 120000:
        tax = tax + (income - 45000) * 0.325 
    else:
        tax = tax + (120000 - 45000) * 0.325 
print(tax)
if income >= 120001:
    if income <= 180000:
        tax = tax + (income - 120000) * 0.37
    else:
        tax = tax + (180000 - 120000) * 0.37
print(tax)        
if income >= 180001:
    tax = tax + (income - 180000) * 0.45
print(tax)