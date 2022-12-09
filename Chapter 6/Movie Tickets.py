while True: #loop for asking the age continously
    age = int(input("Enter the age to find out the ticket price or enter 'quit' to exit.:")) #asks user to enter age

#if-elif-else statement for the ticket price according to the ages
    if age == "quit":
                break
    if age < 3:
        print("Your ticket is free!")
    elif age < 12:
        print("Your ticket is $10!")
    else:
        print("Your ticket is $15")