def falsy(arr):
    trueArr = []
    for entry in arr:
        if bool(entry) is True:
            trueArr.append(entry)
    print(trueArr)
falsy([7, "ate", "", False, 9])