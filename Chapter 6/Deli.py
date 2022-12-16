sandwich_orders = ["tuna", "egg", "chicken", "vegan"] #list of sandwiches
finished_sandwiches = [] #empty list to store popped sandwiches

while sandwich_orders: #loops through the sandwich orders
    sandwich_popped = sandwich_orders.pop() #pops each sandwich
    print(f"Your {sandwich_popped} sandwich is currently in the works!") #informs user that the sandwiches are in the works
    finished_sandwiches.append(sandwich_popped) #adds the popped sandwiches in the empty list

print("\n") #adds whitespace

for sandwich_popped in finished_sandwiches: #displays the finished sandwiches
    print(sandwich_popped.title(),"sandwich is ready!") #informs user that the sandwiches are ready
