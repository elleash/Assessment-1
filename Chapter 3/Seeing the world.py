place = ["Norway", "Italy", "France", "Mexico"] #list of places
print(place) #prints the list

print("\nThe original list is:") #displays message about the list information
print(place) #displays the list

print("\nThis is the list in alphabetical order:") #displays message about the list information
print(sorted(place)) #arranges the list in alphabetical order
print("\nThe original order:") #displays message about the list information
print(place) #displays the list

print("\nThis is the list in reverse order:") #displays message about the list information
print(sorted(place, reverse = True)) #arranges the list in reverse alphabetical order
print("\nThe original order:") #displays message about the list information
print(place) #displays the list

print("\nThis is the list in reverse order:") #displays message about the list information
place.reverse() #reverse the list in order
print(place) #displays the list

print("\nThe original order:") #displays message about the list information
place.reverse() #reverses it back to the original order
print(place) #displays the list

print("\nThis is the list in alphabetical order:") #displays message about the list information
place.sort() #arranges the list in alphabetical order
print(place) #displays the list

print("\nThis is the list in reversed alphabetical oder:") #displays message about the list information
place.sort(reverse = True) #arranges list in reverse alphabetical
print(place) #displays the list
