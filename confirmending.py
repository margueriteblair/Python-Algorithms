def confirm(str, target):
    if slice(str[len(str) - len(target)] == target):
        print(True)
confirm("Hello", "o")
confirm("bastian", "n")