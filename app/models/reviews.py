class Review:
    all_reviews = []

    def __init__(self,news_id,description,urlToImage,review):
        self.news_id = news_id
        self.description = description
        self.urlToImage = urlToImage
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()