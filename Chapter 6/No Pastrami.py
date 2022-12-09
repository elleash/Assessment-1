sandwich_orders = ["tuna", "pastrami", "egg", "chicken","pastrami", "vegan", "pastrami"] #added pastrami in the list
finished_sandwiches = []

print("Unfortunaley, The Deli has run out of pastrami\n")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami") #removes the pastrami in the list

while sandwich_orders:
    sandwich_popped = sandwich_orders.pop() #pops each sandwich in the updated list
    print(f"Your {sandwich_popped} sandwich is currently in the works!")
    finished_sandwiches.append(sandwich_popped) #adds the popped sandwiches in the finished sandwich list

print("\n")

for sandwich_popped in finished_sandwiches: #prints the ready sandwiches
    print(sandwich_popped.title(),"sandwich is ready!")