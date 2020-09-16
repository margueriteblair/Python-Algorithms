def reverse_string(str):
    str_arr = []
    index = len(str) - 1

    while index >= 0:
        str_arr.append(str[index])
        index = index - 1
    print("".join(str_arr))


reverse_string("Hello world")