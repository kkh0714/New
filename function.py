def greet_user(first_name, last_name): # first_name and last_name are parameters
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")

print("Start")
greet_user("John", "Smith") # "John", "Smith" are positional arguments
# keyword argument improves the readability of the code, but usually we use positional arguments
# greet_user(last_name="Smith", first_name="John") #first_name="John" is a keyword argument, the position doesn't matter.
print("Finish")
