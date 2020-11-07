pizza = {}

#add dictionary options for sauce and cheese
pizza["cheese"] = input("Type in your favorite pizza cheese! ")
pizza["sauce"] = input("Type in your favorite pizza sauce! ")
pizza["crust"] = input("Type in your favorite pizza crust! ")
pizza["topping"] = input("Type in your favorite pizza topping! ")

#while topping != "quit":
    #pizza.append(topping)

    #topping = input("Type in your favorite pizza topping! ")

for key, value in pizza.items():
    #print key and value

    print(key, value)