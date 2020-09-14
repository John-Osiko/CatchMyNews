class News:
    """
    News clas to define Movie objects
    """

    def __init__(self,id,source,author,description,urlToImage,publishedAt,content):
        self.id = id
        self.source = source
        self.author = author
        self.description = description
        self.urlToImage = "https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg" + urlToImage
        self.publishedAt = publishedAt
        self.content = content