import unittest
import sys
sys.path.append('./')
from jaccard import jsimilarity
"""
This module is the one that tests the jaccard similarity function.
The Test Case tests a Known valid, empty strings entries and a corner case
with an empty list.
For the testing, we used two lists of random words:
['dog','cat', 'bird'] , ['dog','ant','bee'] ,
an invalid entry with empty strings and an empty list .
"""
class TestJaccard(unittest.TestCase):
    
    # valid inputs
    def test_jaccard_success(self):
        tlist1 = ['dog','cat','bird']
        tlist2 = ['dog','ant','bee']
        actual = jsimilarity(tlist1,tlist2)
        self.assertEqual(actual, 0.2)
        
    # invalid inputs empty strings 
    def test_wrong_values(self):
        # you should input wrong data
        tlist1 = ['dog','cat','bird']
        tlist3 = ["","",""]
        self.assertEqual(jsimilarity(tlist1, tlist3), 0.0)
        
    # corner case: empty list
    def test_empty_list(self):
        tlist1 = ['dog','cat','bird']
        tlist4 = []
        self.assertEqual(jsimilarity(tlist1,tlist4), 0.0)  

if __name__ == '__main__':
    # with more details
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 

