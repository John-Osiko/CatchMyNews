class News:
    """
    News class to define news objects
    """

    def  __init__(self,id,source,author,description,urlToImage,publishedAt,content):
        self.id = id
        self.source = source
        self.author = author
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content



class Sources:
    def __init__(self,source_id,name,description,country):
        self.source_id = source_id
        self.name = name
        self.description = description
        self.country = country
class Review:
    all_reviews = []

    def __init__(self,news_id,description,urlToImage,review):
        self.news_id = news_id
        self.title = title
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