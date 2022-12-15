name = "\n\t  James" #the name with whitespaces
print("My name is", name) #print the string with whitespaces

name = "\n\t  James" #the name with whitespaces
print("My name is", name.strip()) #using .strip function to strip the whole name

name = "\n\t  James" #the name with whitespaces on the left
print("My name is", name.lstrip()) #using .lstrip to strip the left side of the string

name = "James\n\t" #the name with whitespaces on the right
print("My name is", name.rstrip()) #using .rstrip to strip the right side of the string
