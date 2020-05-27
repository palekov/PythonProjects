import pyowm

owm = pyowm.OWM('5c361be8f5a8f221d3918c76f0c0a049')
place = input("В каком городе/стране?:")
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp = w.get_temperature('celsius')["temp"]
print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас " + str(temp))
