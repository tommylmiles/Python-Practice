'''
def make_shirt(size = 'Large',message = 'I Love Python'):
    print(f"Your shirt size is {size}, and will have the message below: \n{message}")


def describe_city(city,country = 'United States'):
    print(f"{city}, is located in the {country}")

describe_city("Richmond")
describe_city("San Francisco")
describe_city('Keiv', country = 'Ukraine')
describe_city('San Juan',"Puerto Rico")

def city_country(city_name,country):
    city_info = f"{city_name}, {country}"
    return city_info

first = city_country("Richmond","USA")
print(first)

def make_album(artist_name, album_title,album_year=None):
    discog = f" \n{artist_name}\n{album_title}\n"
    return discog

while True:
    artist_n = input('Artist Name: ')
    album_n = input('Album Name: ')

    Artwork = make_album(artist_n,album_n)
    print(Artwork)
'''
text_msg = ['Hey There','BRB','New Phone, Who dis?']
empty_msg = []
def show_messages(messages):
        for message in messages:
            print(message)


show_messages(text_msg)

def show_message():
    for txt in text_msg:
        print(txt)
show_message()

def send_message(outbound,inbound):
    while outbound:
        sending = outbound.pop()
        inbound.append(sending)
    print("Done")

send_message(text_msg[:],empty_msg)
print(text_msg)
print(empty_msg)