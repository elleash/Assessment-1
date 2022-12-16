glossary = {"variable": "A variable is a name referring to an object or value.", 
    "string": "A string is series of words or characters.",
    "loop" : "Loops are utilised when we need to run statements repeatedly until a specific condition has been executed.",
    "list" : "A set of values that are mutable and flexible.",
    "dictionary" : "A dictionary is and ordered collection of key-value pairs."} #python dictionary

for key, value in glossary.items(): # loops through the dictionary
   print(key.title(), ":") #prints the word
   print(value, "\n") #prints the meaning of the word

glossary["tuple"] = "A set of values that are immutable." #adding the "tuple" item
glossary["input"] = "A function that allows the user to enter a text." #adding the "input" item
glossary["concatenation"] = "Concatenation adds two string together by using the '+' operator." #adding the "concatenation" item
glossary["print"] = "The print syntax displays the output to the user." #adding the "print" item
glossary["constant"] = "A variable where the value stays the same through the program." #adding the "constant" item

print("\n\nThe updated glossary:\n\n") #a message to inform user of the updated list

for key, value in glossary.items(): #loops through the updated dictionary
   print(key.title(), ":") #prints the word
   print(value, "\n") #print the meaning of the word
