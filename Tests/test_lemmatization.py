import unittest
from stemlem import lemmatization
"""
This module is the one that tests the lemmatization function.
The Test Case tests a Known valid, invalid entries and a corner case
with an empty string.
For the testing, we used a list of random words:
["playing", 'played', 'plays'].
"""
class TestLemmatization(unittest.TestCase):
    
    # valid inputs
    def test_lemmatization_success(self):
        actual = lemmatization(["playing", 'played', 'plays'])
        self.assertEqual(actual, ["playing", 'played', 'play'])
        
    # invalid inputs
    def test_wrong_values(self):
        # you should input wrong data
        #self.assertEqual(lemmatization(["Played"]), None)
        self.assertNotEqual(lemmatization(["Played"]), None)
        
    # corner case: empty string
    def test_empty_string(self):
        self.assertEqual(lemmatization(" "), [] )  

if __name__ == '__main__':
    # with more details
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 
