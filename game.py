import random

color = ["blue", "sky blue", "orange"]
food = ["milk", "poop", "pizza", "cake"]
goodguy = ["Super meow", "The cat man", "Super Bob","Secret agent unicorn"]
badguy = ["Death Girl", "The Evil Meow", "Shadow Bob"]
buildings = ["house", "lab","shop"]

print("One day " + random.choice(goodguy) + " went to the " + random.choice(buildings) + ".")
print("And they saw " + random.choice(badguy))
print("They attacked them with " + random.choice(color) + " " + random.choice(food))
print("And it did " + str(random.randint(0,100)) + " damage")
print("Then they left.THE END.")
