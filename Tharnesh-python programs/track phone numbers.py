import phonenumbers
from phonenumbers import geocoder
phone_number1=phonenumbers.parse("+918667810713")
phone_number2=phonenumbers.parse("+918760747575")
phone_number3=phonenumbers.parse("+919894743513")
print("Phone numbers location:")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
print(geocoder.description_for_number(phone_number3,"en"))
