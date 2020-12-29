n = int(input())
phone_book = dict(input().split() for i in range(n))
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break


N = int(input())
arr_map = {}
for i in range(N):
    x = input().split()
    arr_map[x[0]] = x[1]
while True:
    try:
        inp = input()
        if (arr_map.__contains__(inp)):
            print(inp + "="+arr_map.get(inp))
        else: 
            print("Not found")
    except EOFError as e:
        break