def confirm(str, target):
    if (str[len(str) - len(target)] == target):
        print(True)
    else:
        print(False)
confirm("Hello", "o")
confirm("bastian", "n")
confirm("hello", "y")