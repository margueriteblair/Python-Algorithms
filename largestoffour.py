def largest_num(arr):
    finalarr = []
    index = 0
    for subarr in arr:
        #print(subarr)
        for i in subarr:
            if i > index:
                index = i
        finalarr.append(index)
    print(finalarr)
            

largest_num([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])