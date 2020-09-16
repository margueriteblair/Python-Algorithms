def find_longest_word_length(str):
    arr = str.split()
    longest = ""
    for word in arr:
        print(word, len(word))
        if len(word) > len(longest):
            longest = word
            continue
    print(longest)

find_longest_word_length("The fox jumped over the rabbit")

