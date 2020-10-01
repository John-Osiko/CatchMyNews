import requests,json

def get_news():
    response = requests.get('https://newsapi.org/v2/sources?language=en&apiKey={}')
    if response.status_code == 200:
        news = response.json()
        return news