def titlecase(str):
    lowerstr = str.lower()
    lowerstr = lowerstr.split()
    titleCaseArr = []
    for word in lowerstr:
        word = word[0].upper() + word[1:]
        print(word)
        titleCaseArr.append(word)
    print(" ".join(titleCaseArr))

titlecase("i'm a little tea pot")

resString = input("What string would you like title cased? ")
titlecase(resString)
