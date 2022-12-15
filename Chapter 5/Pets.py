pet1 = {"name":"gambol", "type": "cat", "color":"black", "owner": "Blake" } #dictionary of first pet
pet2 = {"name":"ember", "type": "dog", "color":"yellow", "owner": "Yang" } #dictionary of first pet
pet3 = {"name":"swei", "type": "dog", "color":"black and white", "owner": "Rose" } #dictionary of first pet
pet4 = {"name":"tena", "type": "cat", "color":"white", "owner": "Weis" } #dictionary of first pet

pets = [pet1, pet2, pet3, pet4] #the dictionary in a list

print("Information about my friend's pets:\n") #displays a message to show info about the pets

for pet in pets: #loops through the list of information about the pets
    print("\n") #adds whitespace
    for key, value in pet.items(): #loops through the dictionary
        print(key.title(), ":", value.title()) #displays the dictionary
