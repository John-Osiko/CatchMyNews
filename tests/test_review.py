import unittest
from app.models import Review


class TestReview(unittest.TestCase):
    """
    Test class that test the behaviour of the Review class
    """

    def setUp(self):
        """
        Set up method will run beore every test
        """
        self.new_reviews = Review(null,'',"https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg",'Seahawks fans spent their entire offseason trying to convince the Seattle coaching staff to let Russ Cook be in the team')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_reviews,Review))


    def test_save_review(self):
        self.news_reviews.save_reviews()
        self.new_reviews = Review(null,'',"https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg",'Seahawks fans spent their entire offseason trying to convince the Seattle coaching staff to let Russ Cook be in the team')
        news_reviews.save_reviews()
        self.assertEqual(len(Review.all_reviews),2)


    def test_clear_reviews(self):
        self.news_reviews.save_reviews()
        self.new_reviews = Review(null,'',"https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg",'Seahawks fans spent their entire offseason trying to convince the Seattle coaching staff to let Russ Cook be in the team')
        news_reviews.clear_reviews()
        self.assertEqual(len(Review.all_reviews),1)


    def test_get_reviews(self):
        self.news_reviews.save_reviews()
        self.new_reviews = Review(null,'',"https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg",'Seahawks fans spent their entire offseason trying to convince the Seattle coaching staff to let Russ Cook be in the team')
        news_reviews.save_reviews()
        response = Review.get_reviews("id")
        self.assertEqual(get_reviews.new_reviews)