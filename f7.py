import json
import requests

def jokes():
    lame=requests.get("https://sv443.net/jokeapi/v2/joke/Any").content
    jk=json.loads(lame.decode('utf-8'))
    show_jokes='*Your Joke*\n\n' + "- "+ jk['setup'] + " \n" +"- "+ jk['delivery']

    print(show_jokes)
    return show_jokes