def make_shirt(size = "large", text = "i love python"): #function with default parameters
    print(f'The shirt with the message "{text.title()}" is a {size} shirt') #message to be printed

make_shirt() #prints the message with the default parameter
make_shirt(size = "medium") #prints the message with the default text parameter but with an overwritten size parameter
make_shirt(size = 'small',text = 'lavender haze' ) #prints the message with overwritten default parameters