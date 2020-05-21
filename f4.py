import json
import requests

def news_f1():
    
    news=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=20116a2eaf2b43b983d771b3d78e8572").content
    mydata = json.loads(news.decode('utf-8'))
    
    top_news = '*Latest News India*\n\n'
   
    for i in range(0,6,2):
        top_news = top_news +  "*{}{}* :\n\n{}\n\n".format(str(i+1) + ') ' , mydata['articles'][i]['title'], mydata['articles'][i]['description'])

    print(top_news)
    return  top_news


def news_f2():
    
    news=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=20116a2eaf2b43b983d771b3d78e8572").content
    mydata = json.loads(news.decode('utf-8'))
    
    latest_news = '*Latest News India*\n\n'

    for i in range(10):
        latest_news = latest_news +  "*{}{}*\n\n".format(str(i+1) + ') ' , mydata['articles'][i]['title'])

    print(latest_news)
    return  latest_news