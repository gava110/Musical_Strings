import copy 
def intersection(list1, list2):
    inter1 = set(list1)
    inter2 = set(list2)
    res = len((copy.deepcopy(inter1)).intersection(inter2))
    return res




