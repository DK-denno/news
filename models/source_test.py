import unittest
from source import Sources


class source_test(unittest.TestCase):
    def setUp(self):
        self.new_source = Sources(
            'ABC-news', 'ABC-news', 'https://abc.com', 'us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_data(self):
        self.assertEqual(self.new_source.id, 'ABC-news')
        self.assertEqual(self.new_source.name, 'ABC-news')
        self.assertEqual(self.new_source.url, 'https://abc.com')
        self.assertEqual(self.new_source.country, 'us')


if __name__ == '__main__':
    unittest.main()
