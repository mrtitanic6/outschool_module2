name = "cat"
print(name)

food = ["bread", "ice cream", "pizza"]
number = 10

number2 = 4.2

print(type(food))
print(type(name))
print(type(number))
print(type(number2))

print(len(food))

print(len(name))

print("i like to eat " + food[-1] + " and "  + food[0] )

food[0] = "sushi"
print(food)

food.append("milk")
print(food)

coldstuff = []

coldstuff.append("ice")
coldstuff.append("ice cream ")
coldstuff.append("snow")
print(coldstuff)

coldstuff.insert(1,"super milk")
print(coldstuff)

del coldstuff[0]
print(coldstuff)

saved_frozen_stuff = coldstuff.pop()
print(coldstuff)
print(saved_frozen_stuff)

lunch = food.pop(2)
print(food)
print(lunch)

food.remove("sushi")
print(food)


