import phonenumbers
from text import numbers;
from phonenumbers import geocoder
someNumber=phonenumbers.parse(numbers)
yourLocation=geocoder.description_for_number(someNumber,"en")
print(yourLocation);