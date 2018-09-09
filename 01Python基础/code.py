def comCode():
    if True:
        print("hi")
        print("Julia")
    else:
        print("hi")
        print("Kite")
    print("how are you")


def valueType():
    var = 1;
    print(var, " type :", type(var))
    var = 1.99;
    print(var, " type :", type(var))
    var = "hello"
    print(var, " type :", type(var))

    print(10/3)
    print(10//3)
    print(2 ** 10)

    
def AssignTest():
    Name,Age = "Kin",32
    print(Name,":",Age)
    Name,Age = "Lin","ok"
    print(Name,":",Age)

def StringTest():
    Say = "Hello World" + (" I love you" * 3)
    Path = r"C:\Windows\info.txt"
    print(Say)
    print(Path)

    SubStr = Path[3:-9]
    print(SubStr)

def ListTest():
    Student = ["Kin",31,"List"]
    Student += ["Lin",21]
    print(Student)

def TupleTest():
    
   Student = ("Kin",31,"Tuple")
   Student += ("Lin",21)

   print(Student)


TupleTest()