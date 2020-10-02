import unittest
from app.models import News

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = News("John Biggs","John Biggs","Two alleged crypto traders in Singapore apparently came up with a fool-proof plan","https://gizmodo.com/crypto-traders-cut-out-the-middleman-simply-rob-victim-1845011301","https://i.kinja-img.com/gawker-media/image/upload/c_fill,f_auto,fl_progressive,g_center,h_675,pg_1,q_80,w_1200/li0fkkejdmaugm8v1fkw.jpg","2020-09-10T14:28:00Z")

    def instance_test(self):
        self.assertTrue(isinstance(self.new_article,News))

if __name__ == "__main__":
    unittest.main()