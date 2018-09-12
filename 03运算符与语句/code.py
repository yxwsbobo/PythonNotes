def whileTest():
    num = 3;
    while num:
        print("in")
        num = num-1
    else:
        print("out")

def forTest():
    for n in range(3):
        print(n)
    else:
        print("over")

def declforTest():
    ls = [1,2,3,4,5]

    for i in [x + 20 for x in ls]:
        print("get :",i)
    
    newls = [x + 20 for x in ls if x>2]
    print(newls)

    for n in newls:
        print("new Num:",n)

    print("-------")

    newlns2 = [x + y for x in ls for y in newls]
    print(newlns2)

declforTest()

