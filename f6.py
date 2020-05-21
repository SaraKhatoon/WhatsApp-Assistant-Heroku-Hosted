import json
import requests

def weather1():

    weather=requests.get("http://api.openweathermap.org/data/2.5/weather?q=bangalore&appid=f3ce5794f01aaae839e3405ba8be3687").content
    mywet=json.loads(weather.decode('utf-8'))
    weather_data = '*Climate in bangalore*\n\n'
    
    w1=mywet['main']['temp'] - 273.15
    w2=str(mywet['weather'][0]['description'])
    w3=str(mywet['main']['humidity'])
    w4=str(mywet['main']['pressure'])
    # w5=str(mywet['visibility']/1000) +  "\nVisibility         : " + w5 + "km"
    weather_data=weather_data + "Temperature: " + "{:.2f}".format(w1) + "°C"
    print(weather_data)
    return  weather_data + "\nDescription   : " + w2 + "\nHumidity        : " + w3 +"%" + "\nPressure        : " + w4 + "mb" 