age = int(input("Please enter your age:")) #asks user to enter the age

#if-elif-else chain that determines the person’s stage of life
if age < 2:
    print("OMG! You are a baby!") 
elif age < 4:
    print("You are a cute toddler!")
elif age < 13:
    print("Oh my, you are still a kid!")
elif age < 20:
    print("You are a teenager! Having fun?")
elif age < 65:
    print("You are an adult!")
else:
    print("You are an elder! Take care")