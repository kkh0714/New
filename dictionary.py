customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith" #change the "name" in dictionary
customer["birthdate"] = "Jan 1 1980" #add a new entry "birthdate" to the dictionary
print(customer["name"])
print(customer.get("name"))
print(customer["birthdate"])