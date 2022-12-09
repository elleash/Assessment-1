guest = ["anne sexton", "silvia plath", "virginia woolf"]
for x in guest: #print the guest individually
    print(f"{x.title()}, you are cordially invited to attend a dinner at 6 pm tomorrow.")

print(f"\nUnfortunately,{guest[1].title()} cannot make it to the dinner tonight. \nWe will be joined by a different guest.\n")

guest.remove("silvia plath") #removing a guest in the list
guest.insert(1,"emily dickinson") #inserting a guest in the list

for x in guest: #print the new guest individually
    print(f"{x.title()}, you are cordially invited to attend a dinner at 6 pm tomorrow.")

print(f"\nI apologize. Unfortunately, I can only invite two people over due to unforseen circumstances.\n")

popped_guest = guest.pop(2) #popped a guest from the list 
print(f"{popped_guest.title()}, I am very sorry to inform that you have been removed from the list.\n")

for x in guest: #print the new guests individually
    print(f"{x.title()}, you are cordially invited to attend a dinner at 6 pm tomorrow.")

#deleting the remaining guests on the list
del(guest[0])
del(guest[0])

print(guest) #prints an empty list