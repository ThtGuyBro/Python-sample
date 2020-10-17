def describe_pet(dog):
    print(dog["breed"])

def make_shirt(shirt):
    print(shirt["message"])

def print_nums(num):
    for x in num:
        print(x)

def get_name():
    return input("Enter your name: ")

def city_country():
    city = input("Enter your city: ")
    country = input("Enter your country: ")
    #"Santiago, Chile"
    return f"{city}, {country}"

def main():
    #dog = {"color": "golden", "breed": "retriever"}
    #describe_pet(dog)
    #shirt = {"size" : "adult small", "message" : "Peace and Luv"}
    #make_shirt(shirt)
    #num = [1, 2, 3, 4
    # , 5]
    #print_nums(num)
    #name = get_name()
    #print(name)

    print(city_country())


main()