#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places

place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

print(type(place_1.amenities))
print(type(place_1.user_id))
print(type(place_1.city_id))
print(type(place_1.name))
print(type(place_1.description))
print(type(place_1.number_rooms))
print(type(place_1.number_bathrooms))
print(type(place_1.max_guest))
print(type(place_1.price_by_night))
print(type(place_1.latitude))
print(type(place_1.longitude))
print(type(place_1.amenity_ids))
print(type(place_1.reviews))

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)
place_2.reviews
storage.save()

print("OK")
