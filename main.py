import phonenumbers
import folium
from phonenumbers import geocoder

from text import numbers;

ch_numbers=phonenumbers.parse(numbers,"CH")
yourLocation=geocoder.description_for_number(ch_numbers,"en")
print(yourLocation);
from phonenumbers import carrier
service_number=phonenumbers.parse(numbers,"RO")
print(carrier.name_for_number(service_number,"en"))
KEY="f06ab75bcda245acbdcee89a7abe700d"
from opencage.geocoder import OpenCageGeocode
geocoder=OpenCageGeocode(KEY)
Query=str(yourLocation)
result=geocoder.geocode(Query)
print(result)
latitude=result[0]['geometry']['lat']
longtude=result[1]['geometry']['lng']
print("Latitudinal location of this phone :",latitude)
print("Longitudinal  location of this phone :",longtude)
Mymap=folium.Map(location=[latitude,longtude],zoom_start=9)
folium.Marker([latitude,longtude],popup=yourLocation).add_to(Mymap)
# save map in html file
Mymap.save("mayLocation.html")