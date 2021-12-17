import unittest
import stopwords_del

"""

This module tests the stopwords removal function.
The Test Case tests only a Known valid case with a song since it is the only
input it can receive from the user (it is already parsed and filtered 
according to the presence inside Top500.csv database. For the testing, we used a piece of the 1st verse of "American Idiot"
by Green Day, a song retrievable from the API, and we want to check if the inputted lyrics in string type 
get outputted as list after being processed by the stopremoval function 

"""

class TestStopwords(unittest.TestCase):
    
    # smoketest
    
    def test_stopwords_success(self):
        
        raw="Don't wanna be an american idiot, Don't want a nation under the new media, And can you hear the sound of hysteria the subliminal mind fuck America"
        output=stopwords_del.stopremoval(raw)
        self.assertTrue(type(output)==list)

    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'], exit=False) 