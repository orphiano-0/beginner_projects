from geopy.geocoders import Nominatim
# pip install geopy

# geolocator object with user agent
geolocator = Nominatim(user_agent='geoapiExercises')
# city name from user input
place = input("Please enter a city: ")
# location with geocode
location = geolocator.geocode(place)
# printing
print(location)
