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

valueType()
