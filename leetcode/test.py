from operator import neg
skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
skl.bisect_key_left(-1)