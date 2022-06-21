import unittest
from translator import english_to_french, french_to_english

class firstTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(" "), " ")
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class secondTest(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(" "), " ")
        self.assertEqual(french_to_english("Bonjour"), "Hello")

unittest.main()