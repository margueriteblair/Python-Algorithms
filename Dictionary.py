# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr_map = []
for i in range(N):
    x = input().split()
    y = dict(name= x[0], phoneNumber=x[1])
    arr_map.append(y)
while True:
    try:
        inp = input()
        if (inp == ""):
            break
        for dictionary in arr_map:
            if (dictionary["name"] == inp):
                print(inp + "=" +dictionary["phoneNumber"])
        
    except EOFError as e:
        break


n = int(input())
phone_book = dict(input().split() for _ in range(n))
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break