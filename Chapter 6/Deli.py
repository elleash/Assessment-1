sandwich_orders = ["tuna", "egg", "chicken", "vegan"]
finished_sandwiches = []

while sandwich_orders:
    sandwich_popped = sandwich_orders.pop() #pops each sandwich
    print(f"Your {sandwich_popped} sandwich is currently in the works!")
    finished_sandwiches.append(sandwich_popped) #adds the popped sandwiches in the finished sandwich list

print("\n")

for sandwich_popped in finished_sandwiches: #prints the ready sandwiches
    print(sandwich_popped.title(),"sandwich is ready!")   