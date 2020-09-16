class News:
    """
    News class to define news objects
    """

    def  __init__(self,id,source,author,description,urlToImage,publishedAt,content):
        self.id = id
        self.source = source
        self.author = author
        self.description = description
        self.urlToImage = "https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg" + urlToImage
        self.publishedAt = publishedAt
        self.content = content


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

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response