from typing import List

car = "subaru"
if car == "subaru":
    print("The car is subaru")
food = "Hot"
food == "Hot"

candace = "Wife"
bernice = "Mother"

if candace == "Wife" and bernice == "Mother":
    print("Welcome you are related to Thomas")

states: List[str] = ["NY","VA","NJ","FL","CA"]
if "CT" in states:
    print("We found New York in the list")
else:
    print("We did not find New York")

age = 20

if age < 2:
    print("You're a baby!")
elif age < 4:
    print("You're a toddler!")
elif age < 13:
    print("You're a kid!")
elif age < 20:
    print("You're a teenager!")
elif age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

current_users = ["Tommy","Cammy","Thomas","Candace","Jill"]
new_users = ["Thomas","Catrina","Celina","Tommy","Bernice"]

testing_users = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in testing_users:
        print(f"{new_user} is already being used")
    else:
        print(f"{new_user}, is being added to the list")


numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1 :
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
