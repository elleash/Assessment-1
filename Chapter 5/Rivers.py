river = {"nile":"egypt", "amazon":"colombia", "mississippi": "illinois"} #dictionary of rivers

for key, value in river.items(): #to iterate the dictionary
   print("The",key.title(), "River runs through",value.title()) #displays message with the key and value items

print("\n") #to add whitespace

for key in river.keys(): #to iterate the dictionary
   print(key.title(), "is a major river of the world!") #displays the river only with the message

print("\n") #to add whitespace

for value in river.values(): #to iterate the dictionary
    print(value.title(), "is the country the river passes through!") #displays the country only with the message
