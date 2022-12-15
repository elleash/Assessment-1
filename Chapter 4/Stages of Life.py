age = int(input("Please enter your age:")) #asks user to enter the age

if age < 2: #if statement for when user is below 2
    print("OMG! You are a baby!") #message to display if user is below 2
elif age < 4: #elif statement for when user is below 4 
    print("You are a cute toddler!") #message to display if user is below 4
elif age < 13: #elif statement for when user is below 13
    print("Oh my, you are still a kid!") #message to display if user is below 13
elif age < 20: #elif statement for when user is below 20
    print("You are a teenager! Having fun?") #message to display if user is below 20
elif age < 65: #elif statement for when user is below 65
    print("You are an adult!") #message to display if user is below 65
else: #else statement for when the user is above 65
    print("You are an elder! Take care") #message to display if user is above 65
