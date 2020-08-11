candace = {
    'first_name':'Candace',
    'last_name':'Miles',
    'age': 33,
    'City':'Dumfries',
    }
tommy = {
    'first_name':'Thomas',
    'last_name':'Miles',
    'age': 35,
    'City':'Richmond',
    }
camryn = {
    'first_name':"Cammy",
    'last_name':"Miles",
    'age': 5,
    'City':'Fairfax',
    }

people = [candace,tommy,camryn]

for person in people:
    name = (f"\n{person['first_name']} {person['last_name']}")

    print(f"{name} is {person['age']} years old and from {person['City']}")



dogs = {
    'typeOfAnimal':'Black Lab',
    'owner':'Candace Miles',
    }
fish = {
    'typeOfAnimal':'Neon Fish',
    'owner': 'Tommy Miles',
    }

pets = []
pets.append(dogs)
pets.append(fish)

for pet in pets:
    print(f"\nThis {pet['typeOfAnimal']} belongs to {pet['owner']}")

favorite_places = {
    'Candace': ['New York','Orlando','Virginia Beach'],
    'Thomas': ['Myrtle Beach','New York','Florida'],
    'Kids': ['Home'],
    }

for names,place in favorite_places.items():
    print(f"{names}'s favorite places to go are:")
    for love in place:
        print(f"\t{love}")

fav_numbers = {
    'tommy': [3],
    'candace': [7,13],
    'cammy': [1,3,10],
    }
for name,number in fav_numbers.items():
    if len(number) == 1:
        print(f"\n{name}'s favorite number is {number}")
    else:
        print(f"\n{name}'s favorite numbers are {number}")

cities = {
    'New York' : {
        'country': 'USA',
        'population': 1000000,
        'fact': 'Big Dirty Apple',
    },
    'Los Angeles': {
        'country': 'USA',
        'population': 100000,
        'fact': 'Where all the movies stars live',
    },
}

for city,city_info in cities.items():
    print(f"\n{city}")
    for facts in city_info:
        print(f"{facts}:{city_info[facts]}")