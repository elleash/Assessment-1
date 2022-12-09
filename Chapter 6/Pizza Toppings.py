while True: #loop to ask user continuosly 
    pizza = input("Enter the toppings you want on your pizza!\nIf you are done, type quit\n") #asks user to enter toppings

    if pizza == "quit": #if they enter "quit" the loop will stop
                break
    else:
        print(f"{pizza} will be added to your pizza!") #users pizza will be added