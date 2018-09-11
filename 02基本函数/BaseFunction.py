
def printWithEnd():
    print("Hello",end=" ")
    print("World")
    print("i'm fine",end=". by Kin")
    print("")
    Say = "hello words"
    print(Say," lentgh :",len(Say))
    Say = "你好"
    print(Say," Length :",len(Say))

def TupleTest():
    Studen = ("Kin",)
    print(Studen)
    Studen = Studen *4
    print(Studen)

def minmaxTest():
    Numbers = ("3","53","21")
    print(max(Numbers))
    print(min(Numbers))

def strTest():
    TupleTest = ("Name","Age")
    strTuple = str(TupleTest)
    print(strTuple," type :",type(strTuple))

    DictionariesTest = {"Name":"Kin","Age":31}
    strDic = str(DictionariesTest)
    print(strDic," type:",type(strDic))

strTest()
