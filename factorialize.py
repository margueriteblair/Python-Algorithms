def factorialize(num):
    total = 1
    for i in range(1, num+1):
        total = total * i
    print(total)

factorialize(5)

def factorialize2():
    q = input('What number would you like to factorialize? ')
    total = 1
    for i in range(1, int(q)+1):
        total = total * i
    print(total)
factorialize2()
