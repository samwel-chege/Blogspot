import unittest
from app.models import Quote

class QuoteModelTest(unittest.TestCase):
    def setUp(self):
        self.new_quote= Quote(author="sammiesam", id=1, quote="coding advice")

    def test_instance(self):
         self.assertTrue(isinstance(self.new_quote, Quote))

    def test_initialization(self):
        self.assertEqual(self.new_quote.author, 'sammiesam' )
        self.assertEqual(self.new_quote.quote, 'coding advice' )