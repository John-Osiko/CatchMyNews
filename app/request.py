from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(category):
    """
    Function that gets the json response to our url request
    """
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
    """
    Function that processes the news feed results and transform them to a list of objects

    Args:
        news_list : A list of dictionaries that containthe movie details

    Returns:
        news_results : A list of news objects
    """
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        source = news_item.get('source')
        author = news_item.get('author')
        description = news_item.get('description')
        urlToImage = news_item.get('image_path')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')

        if urlToImage:
            news_object = News(id,source,author,description,urlToImage,publishedAt,content)
            news_results = append(news_object)


    return news_results


def get_news_feed(id):
        get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            source = news_details_response.get('source')
            author = news_details_response.get('author')
            description = news_details_response.get('description')
            urlToImage = news_details_response.get('image_path')
            publishedAt = news_details_response.get('publishedAt')
            content = news_item.get('content')

            news_object = News(id,source,author,description,urlToImage,publishedAt,content)


    return news_object


def search_news(news_name):
    search_news_url = 'http://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=42ff49abe2dd44e08eb28ab10b3103a6&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_respomse = json.loads(search_news_data)

        search_news_results = None

        if search_news_respomse['results']:
            search_news_list = search_news_respomse['result']
            search_news_results = process_results(search_news_list)


    return search_news_results