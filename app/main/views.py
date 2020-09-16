from flask import render_template,request,redirect,url_for
from app import app
from request import get_news, get_news_feed,search_news
from models import review
from forms import ReviewForm
Review = review.Review


# Views
@app.route('/')
def index():
    
    '''
    View root page function that returns the index page and its data
    '''

     # Getting popular movie
    latest_news = get_news('latest')
    news_bulleting = get_news('bulletings')
    news_at_moment = get_news('now_playing')
    title = 'Home - Welcome! This is your no.1 news feed Website Online'
    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))

    else:
        return render_template('index.html', title = title, latest_news = latest, news_bulleting = bulletings, news_at_moment = now_playing)


@app.route('/news/<news_id>')
def news(news_id):

    '''
    View movie page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)
    news = get_news(id)
    description = f'{news.description}'
    reviews = Review.get_reviews(news.id)

    return render_template('news.html', description = description, news = news, reviews = reviews)


@app.route('/search/<news_name>')
def search(news_name):
    """
    View function to display the search results
    """
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)


@app.route('/news/review/new/<int:id>',methods = ['GET', 'POST'])
def news_feed_review(id):
    form = ReviewForm()
    news = get_news(id)

    if form.validate_on_submit():
        description = form.description.data
        review = form.review.data
        news_feed_review = Review(news.id,description,news.urlToImage,review)
        news_feed_review.save_review()
        return redirect(url_for('news',id = news.id))
    title = f'{ news.description} review'
    return render_template('news_feed_review.html',description = description, review_form = form, news = news)
