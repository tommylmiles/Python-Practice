my_food = ["pizza","cake","beef"]
friend_foods = my_food[:]
my_food.append("cheese")
friend_foods.append("Meatloaf")
favs = "My Favorite foods are:"
for food in my_food:
    print(food)

buffet_food = ("chicken","burger","fries","cake","hotdog")
print("Here are some foods from the buffet:")
for food in buffet_food:
    print(f"-{food}")