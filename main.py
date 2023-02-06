import random
destination_options = ['Mexico', 'France', 'Africa']
restaurant_options = ['chain', 'local', '5star']
transportation_options = ['own 2 feet', 'cab', 'scooters']
entertainment_options = ['guided tour', 'swimming', 'karaoke night']


day_trip_is_running = True 
while day_trip_is_running == True:
    destination = random.choice(destination_options)
    restaurant = random.choice(restaurant_options)
    transportation = random.choice(transportation_options)
    entertainment = random.choice(entertainment_options)

    completed_trip = {
        "DESTINATION": destination,
        "RESTAURANT": restaurant,
        "TRANSPORTATION":transportation,
        "ENTERTAINMENT": entertainment
    }
    print(completed_trip)
    user_input = input("You happy with this?")
    if user_input == "y":
        day_trip_is_running = False
    
    