#Type you age into person to find out who you are!

person = int(input("Type you age into person to find out who you are! "))
while person != 0:
    if person < 2:
        print("You are a baby")
    elif 4 > person >= 2:
        print("You are a toddoler")
    elif 13 > person >= 4:
        print("You are a kid")
    elif 20 > person >= 13:
        print("You are a teenager")
    elif 65 > person >= 20:
        print("You are an adult")
    elif 100 > person >= 65:
        print("You are an elder")
    elif person >= 100:
        print("You are dead")

    person = int(input("Type you age into person to find out who you are! "))