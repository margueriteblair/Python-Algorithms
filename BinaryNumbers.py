if __name__ == '__main__':
    n = int(input())
    ten = (bin(n)[2:])
    max1 = 0
    consec = 0
    for i in range(len(ten)):
        if (ten[i] == "1"):
            consec = consec+1
            if (consec > max1):
                max1 = consec
        else:
            consec = 0
    print(max1)