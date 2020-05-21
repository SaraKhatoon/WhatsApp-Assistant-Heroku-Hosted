import json
import requests

def namaz():
    lame2=requests.get("http://api.aladhan.com/v1/calendarByCity?city=Bangalore&country=India&method=2&month=01&year=2020").content
    timings=json.loads(lame2.decode('utf-8'))
    nt='*Namaz Timings*\n\n' +"Fajr : "+  timings['data'][0]['timings']['Fajr'] + " \n" +"Sunrise : "+  timings['data'][0]['timings']['Sunrise'] + " \n" + "Zohr : "+ timings['data'][0]['timings']['Dhuhr'] + " \n"+"Asr : "+  timings['data'][0]['timings']['Asr'] +"\n"+"Sunset : "+  timings['data'][0]['timings']['Sunset']  + " \n" +"Maghrib : "+  timings['data'][0]['timings']['Maghrib'] + " \n" +"Isha : "+  timings['data'][0]['timings']['Isha']  

    print(nt)
    return nt