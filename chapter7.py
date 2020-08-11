#car = input("Please let me know what kind of rental you would like: ")
#print(f"Let me see if we have any {car}'s available")

#attend = input("How many is in your party? : ")
#attend = int(attend)

#if attend >= 8:
#    print("Sorry there is a long wait")
#else:
#    print("Please walk this way")
"""
number = input("Please enter a Number: ")
number = int(number)

if number % 10 == 0:
    print(f"Yay {number} is a multiple of 10")
else:
    print(f"Sorry, {number} is not a factor of 10")


current_number = 0
while current_number < 10:
    if current_number % 2 == 0:
        current_number += 1
    else:
        print(current_number)
        current_number += 1

toppings = []
while True:
    topper = input("Please enter a pizza topping: ")
    if topper == 'quit'.lower():
        print(toppings)
        break
    else:
        toppings.append(topper)
"""
'''
flag = True

while flag:

    mticket = input("Please enter in your age: ")

    if mticket == 'quit':
        flag = False
    else:
        mticket = int(mticket)
        if mticket < 3:
            print("Your ticket is free")
        elif mticket < 13:
            print("Your ticket cost $10")
        else:
            print("Your ticket is $15 dollars")
'''
'''
sandwich_orders = ['pastrami','BLT','pastrami','Cuban','Ham and Cheese','pastrami']
finished_sandwiches = []
print("We are all out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    making = sandwich_orders.pop()
    print(f"I made your {making} sandwich")
    finished_sandwiches.append(making)
for done_food in finished_sandwiches:
    print(f"{done_food} - completed")
'''

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name: ")
    dream = input("What is your dream destination: ")
    responses[name] = dream
    repeat = input("Do you want to continue: (Y/N)")

    if repeat == 'N':
        polling_active = False
    elif repeat == 'Y':
        continue
    else:
        print("Invalid")
        break

print("Here are the results for the polling: ")

for name,dream in responses.items():
    print(f"{name},would love to visit {dream}")