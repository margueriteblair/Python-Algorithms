def repeat_a_string(str, num):
    final = []
    i = 0
    while i < num:
        final.append(str)
        rpt = "".join(final)
        i = i + 1
    print(rpt)

repeat_a_string("abc", 3)