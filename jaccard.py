import copy
def jsimilarity(list1, list2):
    jacc1 = set(list1)
    jacc2 = set(list2)
    inter= (copy.deepcopy(jacc1)).intersection(jacc2)
    union= jacc1.union(jacc2)
    res = float (len(inter)/len (union))
    return res

