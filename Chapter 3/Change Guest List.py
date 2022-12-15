guest = ["anne sexton", "silvia plath", "virginia woolf"] #list of guest

for x in guest: #prints the guest in the list individually
    print(f"{x.title()}, you are cordially invited to attend a dinner at 6 pm tomorrow.") #display a message of guests being invited

print(f"\nUnfortunately,{guest[1].title()} cannot make it to the dinner tonight. \nWe will be joined by a different guest.\n") #display a message of a guest not making it and is being replaced by a different guest

guest.remove("silvia plath") #removing a guest in the list
guest.insert(1,"emily dickinson") #inserting a different guest

for x in guest: #prints the guest in the list individually
    print(f"{x.title()}, you are cordially invited to attend dinner at 6pm tomorrow.") #display message of the guests with the new guest
