place = ["Norway", "Italy", "France", "Mexico"]
print(place)

print("\nThe original list is:")
print(place)

print("\nThis is the list in alphabetical order:")
print(sorted(place)) #arranges the list in alphabetical order
print("\nThe original order:")
print(place)

print("\nThis is the list in reverse order:")
print(sorted(place, reverse = True)) #arranges the list in reverse alphabetical order
print("\nThe original order:")
print(place)

print("\nThis is the list in reverse order:")
place.reverse() #reverse the list in order
print(place)

print("\nThe original order:")
place.reverse() #reverses it back to the original order
print(place)

print("\nThis is the list in alphabetical order:")
place.sort() #arranges the list in alphabetical order
print(place)

print("\nThis is the list in reversed alphabetical oder:")
place.sort(reverse = True) #arranges list in reverse alphabetical
print(place)