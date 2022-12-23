while True: #loop for asking the age continously
    age = int(input("Enter the age to find out the ticket price: ")) #asks user to enter age

    if age < 3: #if user is below 3, then the ticket is free
        print("Your ticket is free!") #displays the ticket price according to age
    elif age < 12:  #if user is below 12, then the ticket is $10
        print("Your ticket is $10!") #displays the ticket price according to age
    else:  #if user is above 12, then the ticket is $15
        print("Your ticket is $15") #displays the ticket price according to age
