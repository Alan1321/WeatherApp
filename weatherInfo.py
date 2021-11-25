import requests

class weatherinfo:
    def __init__(self,city):
        self.city = city
        self.api = "http://api.openweathermap.org/data/2.5/weather?q=" + self.city + "&appid=1ab2ff5d58fef6e31da66ca9b0c71998"
        self.json_data = requests.get(self.api).json()

    def toString(self):
        city_name = format("Location:", "16") + self.city.capitalize()
        wind_speed = format("Wind Speed:", "13") + str(self.json_data['wind']['speed'])
        humidity = format("Humidity:", "15") + str(self.json_data['main']['humidity'])
        longitude = format("Longitude:", "14") + str(self.json_data['coord']['lon'])
        latitude = format("Latitude", "16") + str(self.json_data['coord']['lat'])
        temp = format("Temperature:", "13") + str(format(self.to_farenheit(self.json_data['main']['temp']), ".2f"))+ " °F"

        data1 = city_name + '\n' + temp + '\n' + wind_speed + '\n' + humidity + '\n'
        data2 = longitude + '\n' + latitude + '\n'

        return data1+data2

    def to_farenheit(self,kelvin):
        number = (kelvin - 273.15) * 9 / 5
        number = number + 32
        return number