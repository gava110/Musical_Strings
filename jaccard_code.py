def jsimilarity(list1, list2):
    jacc1 = set(list1)
    jacc2 = set(list2)
    res = float(len(jacc1.intersection(jacc2)) / len(jacc1.union(jacc2)))
    return res

