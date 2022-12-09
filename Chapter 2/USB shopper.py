girl = 50 #the girl money
usb = 6 #the usb price

bought = girl // usb #the formula for finding the number of usb she can get with her money
pounds = girl % usb #the formula for finding out how much money she will have left

print("The number of USB the girl can get is",bought, f"and she will have £{pounds} left!")