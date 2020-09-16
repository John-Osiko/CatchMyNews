import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    """
    Test class that test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method will run beore every test
        """
        self.new_news = News(null,'CBS Sports','','NFL Week 1 grades: Seahawks get an A for letting Russell Wilson cook, Cowboys earn a B- despite loss - CBS Sports','Here are the Week 1 grades for every team that played on Sunday',"https://sportshub.cbsistatic.com/i/r/2020/09/13/188a128c-86a2-4cda-8108-a3462b320695/thumbnail/1200x675/4d9d897b1c84402c4a3c5f5e72c69a02/russell-wilson-seahawks.jpg",'2020-09-14T03:45:00Z','Seahawks fans spent their entire offseason trying to convince the Seattle coaching staff to Let Russ Cook, and based on Sunday opener in Atlanta, it appears that the team finally decided to let Rus… [+3146 chars]')


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))