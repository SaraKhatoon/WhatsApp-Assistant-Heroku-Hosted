import json
import requests

def quotes():
    lame1=requests.get("https://api.quotable.io/random").content
    qt=json.loads(lame1.decode('utf-8'))
    kots='*Your Quote*\n\n' +  qt['content'] + " \n" +"- "+ qt['author']

    print(kots)
    return kots