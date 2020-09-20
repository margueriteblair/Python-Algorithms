def sliceandsplice(arr1, arr2, n):
    new_arr = [*arr2[:n], *arr1, *arr2[n:]]
    
    print(new_arr)


sliceandsplice([1, 2, 3], [4, 5, 6], 1)
sliceandsplice([1, 2, 3], [4, 5], 1)