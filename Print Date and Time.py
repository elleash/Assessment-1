import  datetime #importing date and time module
now = datetime.datetime.now() #importing date and time module
print("The current date and time :") #print statement to display the current date and time
print(now.strftime("%Y-%m-%d %H:%M:%S")) #for specifying the format