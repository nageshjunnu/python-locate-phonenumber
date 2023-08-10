import phonenumbers
from phonenumbers import geocoder
import folium
from test import number

number=input("Enter number with country code:")
check_number = phonenumbers.parse(number)
number_location= geocoder.description_for_number(check_number, "en")
print(number_location)

from phonenumbers import carrier

service_provider=phonenumbers.parse(number)

print(carrier.name_for_number(service_provider, "en"))

key="7ec6715f115844b1b582c0b1424a8d40"
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query=str(number_location)

results = geocoder.geocode(query)

lat= results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']

print(results[0]['formatted'])

print(lat,lng)

map_location=folium.Map(location=[lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")