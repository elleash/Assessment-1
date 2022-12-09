#dictionary of pets
pet1 = {"name":"gambol", "type": "cat", "color":"black", "owner": "Blake" }
pet2 = {"name":"ember", "type": "dog", "color":"yellow", "owner": "Yang" }
pet3 = {"name":"swei", "type": "dog", "color":"black and white", "owner": "Rose" }
pet4 = {"name":"tena", "type": "cat", "color":"white", "owner": "Weis" }

pets = [pet1, pet2, pet3, pet4] #the dictionary in a list

print("Information about my friend's pets:\n")

for pet in pets: #loops through the list of information about the pets
    print("\n")
    for key, value in pet.items(): 
        print(key.title(), ":", value.title())
