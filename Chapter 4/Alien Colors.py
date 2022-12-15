alien_color = "green" #version that passes

if alien_color == "green": #if the variable is green then the player earns 5 points
    print("You just earned 5 points!") #message displayed if the variable is green

alien_color = "yellow" #version that fails

if alien_color == "green": #if statement to test the failed code
    print("You just earned 5 points!") #message displayed if the variable is green
