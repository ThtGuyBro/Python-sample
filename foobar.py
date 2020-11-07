water = 30

for num in range(1, water + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("foobar")
    elif num % 3 == 0:
        print ("foo")
    elif num % 5 == 0:
        print("bar")
    else: 
        print(num)