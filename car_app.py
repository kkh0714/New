command = ""

start = False
stop = True

# This line of code is not okay because it will always show else statment before ending the while loop
# while command.lower() != "quit":
while True:
    command =  input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
        """)
    elif command == "start":
        if start == True:
            print("Car is already started.")
        else:
            print("Car started...Ready to go!")
            start = True
            stop = False
    elif command == "stop":
        if not start:
            print("Car is already stopped.")
        else:
            print("Car stopped.")
            start = False
            stop = True
    elif command == "quit":
        break
    else:
        print("I don't understand that...")



