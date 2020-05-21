import json
import requests
def corona():
    virus=requests.get("https://api.covid19api.com/summary").content
    covid=json.loads(virus.decode('utf-8'))
    corona_news='*Covid-19 News*\n\n' + "- "+ "*Global Covid Cases :*" + "\n" + "   Total Confirmed : " + str(covid['Global']['TotalConfirmed']) + "\n" + "   Total Deaths : " + str(covid['Global']['TotalDeaths']) + "\n" + "   Total Recovered : " + str(covid['Global']['TotalRecovered']) + "\n\n"+"- " +  "*India Covid Cases :*" + "\n"+"   Total Confirmed : " + str(covid['Countries'][101]['TotalConfirmed']) + "\n" + "   Total Deaths : " + str(covid['Countries'][101]['TotalDeaths']) + "\n" + "   Total Recovered : " + str(covid['Countries'][101]['TotalRecovered'])
    
    print(corona_news)
    return corona_news