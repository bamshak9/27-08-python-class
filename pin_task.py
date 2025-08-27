correct_pin = 7732
i=1
while i<4:
    pin =int(input("What is your pin: "))
    if pin == correct_pin:
        print("Access Granted")
        i=10
    elif pin != correct_pin and i>=3:
        print("Card blocked")

    i+=1
#f i>=4:
 #  print("Card blocked")

