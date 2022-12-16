sandwich_orders = ["tuna", "pastrami", "egg", "chicken","pastrami", "vegan", "pastrami"] #added pastrami in the list
finished_sandwiches = [] #empty list to store sandwich orders

print("Unfortunaley, The Deli has run out of pastrami\n") #displays a message that informs there are no more pastrami
while "pastrami" in sandwich_orders: #loops through the list
    sandwich_orders.remove("pastrami") #removes the pastrami in the list

while sandwich_orders: #loops through the sandwich_orders list
    sandwich_popped = sandwich_orders.pop() #pops each sandwich in the updated list
    print(f"Your {sandwich_popped} sandwich is currently in the works!") #informs user that the sandwich is in works
    finished_sandwiches.append(sandwich_popped) #adds the popped sandwiches in the finished sandwich list

print("\n") #adds whitespace

for sandwich_popped in finished_sandwiches: #displays the finished sandwiches
    print(sandwich_popped.title(),"sandwich is ready!") #informs the user that the sandwich is ready
