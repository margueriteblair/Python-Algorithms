def diagonalDifference(arr):
    sumLeft = 0;
    for j in range(0, len(arr)):
        for i in range(0, len(arr[0])):
            if (i == j):
                sumLeft += arr[i][j];
    sumRight = 0;
    for j in range(0, len(arr)):
        for i in range(0, len(arr[0])):
            if (i+j == len(arr[0])-1):
                sumRight += arr[i][j];
    return abs(sumLeft-sumRight)