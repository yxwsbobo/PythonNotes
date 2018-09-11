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

    Student = ("Name","Age","type")
    print(Student)
    Student = list(Student)
    print(Student)

def TupleTest():
    
   Student = ("Kin",31,"Tuple")
   Student += ("Lin",21)

   print(Student)

   Student =["Name","Age","language"]
   print(Student)
   Student = tuple(Student)
   print(Student)


def DictionTest():
    Maps = {"Name":"Kin","Age":32,"Score":85}
    if("Name" in Maps):
        print("Maps have Key Name")
    else:
        print("Maps haven't Key Name")
    
    del Maps["Name"]

    if("Name" in Maps):
        print("Maps have Key Name")
    else:
        print("Maps haven't Key Name")

    print(Maps.keys())
    print(Maps.values())

