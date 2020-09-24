def find_longest_word_length(str):
    arr = str.split()
    longest = ""
    for word in arr:
        print(word, len(word))
        if len(word) > len(longest):
            longest = word
    print(len(longest))

# find_longest_word_length("The fox jumped over the rabbit")

resStr = input("Please input in a string: ")
find_longest_word_length(resStr)

def longestWord3():
    string = input('Enter sentence to find longest word\n')
    strSplit = string.split()
    strSplit.sort(key = len)
    print(strSplit[-1]) #-1 index will be the last element in list


