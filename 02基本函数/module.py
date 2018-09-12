import keyword
import collections
def keyList():
    print(keyword.kwlist) #关键字列表

def dequeTest():
    var = collections.deque([3,4,5,6])

    print(var)
    print(type(var))

dequeTest()

