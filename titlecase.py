def titlecase(str):
    lowerstr = str.lower()
    lowerstr = lowerstr.split()
    titleCaseArr = []
    for word in lowerstr:
        word = word[0].upper() + word[1:]
        titleCaseArr.append(word)
    print(" ".join(titleCaseArr))

titlecase("I'm a little tea pot")