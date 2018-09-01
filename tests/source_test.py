import unittest
from app.models importimport Sources


class source_test(unittest.TestCase):
    '''
    this function creates an object of the Sources class before each and every tesy
    '''
    def setUp(self):
        self.new_source = Sources(
            'ABC-news', 'ABC-news', 'https://abc.com', 'us')

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
        self.assertEqual(self.new_source.url, 'https://abc.com')
        self.assertEqual(self.new_source.country, 'us')


if __name__ == '__main__':
    unittest.main()
