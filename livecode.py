# Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.

# Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].

def largest_of_four(arr):
    finalArr = []
    index = 0
    for subArr in arr:
        for i in subArr:
            if i > index:
                index = i
        finalArr.append(index)
    
    print(finalArr)


largest_of_four([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])
largest_of_four([[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]])