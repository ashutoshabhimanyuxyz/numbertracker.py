import phonenumbers
from phonenumbers import geocoder
no=input("phone num:")
number=phonenumbers.parse(no)
print(geocoder.description_for_number(number,"en"))