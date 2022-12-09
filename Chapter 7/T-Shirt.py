def make_shirt(size,text): #function with two parameters
    print(f'The size of this shirt is {size} and the text "{text.title()}" is written on it') #message to be printed

make_shirt("large", "August slipped away like a moment in time, cause it was never mine") #prints the message using positional arguments
make_shirt(size = "extra large", text = "tell me that im all you want even when i break your heart") #prints the message using keyword arguments