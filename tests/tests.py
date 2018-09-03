import unittest
from app.models import Headlines,Sources

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

class source_test(unittest.TestCase):
    '''
    this function creates an object of the Sources class before each and every tesy
    '''
    def setUp(self):
        self.new_source = Sources(
            'ABC-news', 'ABC-news','dk', 'https://abc.com', 'us')

    def test_instance(self):
        '''
        this is a function to assert whether the instance is really an instance of our class
        '''
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_data(self):
        '''
        this function asserts whether the value entered by the setUp method will apper if the property is called
        '''
        self.assertEqual(self.new_source.id, 'ABC-news')
        self.assertEqual(self.new_source.name, 'ABC-news')
        self.assertEqual(self.new_source.desc,'dk')
        self.assertEqual(self.new_source.url, 'https://abc.com')
        self.assertEqual(self.new_source.country, 'us')
       

if __name__ == '__main__':
    unittest.main()