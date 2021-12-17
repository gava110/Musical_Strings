import copy
"""
This function called jsimilarity will take two lists
as input from previous code, containing the lyrics of
the two songs chosen by the user,
and return the jaccard similarity value
between the two songs.
"""


def jsimilarity(list1, list2):

    jacc1 = set(list1)
    jacc2 = set(list2)

    # intersection between the two songs 
    inter = (copy.deepcopy(jacc1)).intersection(jacc2)
    
    # union between the two songs
    union = jacc1.union(jacc2)
    
    # jaccard similarity formula
    res = float(len(inter) / len(union))
    
    # jaccard similarity value
    return res
