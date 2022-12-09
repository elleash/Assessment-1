river = {"nile":"egypt", "amazon":"colombia", "mississippi": "illinois"} #dictionary of rivers

for key, value in river.items(): #prints the dictionary
   print("The",key.title(), "River runs through",value.title())

print("\n")

for key in river.keys(): #prints the river only
   print(key.title(), "is a major river of the world!")

print("\n")

for value in river.values(): #prints the coutry only
    print(value.title(), "is the country the river passes through!")