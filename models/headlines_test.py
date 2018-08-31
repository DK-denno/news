import unittest
from headlines import Headlines

class headlines_test(unittest.TestCase):
    def setUp(self):
        self.new_headline = Headlines('a','b','c','d','e','f')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,Headlines))
    
    def test_True(self):
        self.assertEqual(self.new_headline.author,'a')
        self.assertEqual(self.new_headline.title,'b')
        self.assertEqual(self.new_headline.description,'c')
        self.assertEqual(self.new_headline.url,'d')
        self.assertEqual(self.new_headline.urlToImage,'e')
        self.assertEqual(self.new_headline.publishedAt,'f')


if __name__ == '__main__':
    unittest.main()