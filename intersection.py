import copy
"""
This function called intersection will take two lists as input
from previous code and return the intersection value
between the words provided in the two lists.
"""


def intersection(list1, list2):
    
    inter1 = set(list1)
    inter2 = set(list2)
    
    # intersection formula between the two lists
    res = len((copy.deepcopy(inter1)).intersection(inter2))
    
    # intersection value
    return res
