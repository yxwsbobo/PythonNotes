import graphics
import myMoudle
import math

def main():
    win = graphics.GraphWin("MyWindow",400,399,True)
    pt1 = graphics.Point(50,60)
    pt2 = graphics.Point(140,100)

    pt1.draw(win)
    pt2.draw(win)

    cc = graphics.Circle(graphics.Point(100,100),40)
    cc.setOutline("red")
    cc.setFill("Blue")
    cc.draw(win)

    txt = graphics.Text(graphics.Point(100,100),"Hello")
    txt.draw(win)

    rtg = graphics.Rectangle(graphics.Point(60,60),graphics.Point(80,80))
    rtg.draw(win)

    line = graphics.Line(graphics.Point(50,200),graphics.Point(100,300))
    line.draw(win)
    
def GetMoneyList(Money,AddApr,Year = 10):
    Result = list()
    for i in range(Year+1):
        Result.append(Money)
        Money = Money *(1 + AddApr)
    return Result

def ptMoneyMap():
    MainWin = graphics.GraphWin("MoneyMap",800,700)
    MoneyList = GetMoneyList(100,0.1,18)
    line = graphics.Line(graphics.Point(80,20),graphics.Point(80,600))
    line.draw(MainWin)
    for y in range(600,30,-20):
        kline = graphics.Line(graphics.Point(80,y),graphics.Point(88,y))
        kline.draw(MainWin)
        txt = graphics.Text(graphics.Point(60,y),str(600 - y))
        txt.draw(MainWin)

    x = 100
    YearNum = 0
    for CurrentMoney in MoneyList:
        StartPoint = graphics.Point(x,600 - CurrentMoney)
        x+=15
        YearTxt = graphics.Text(graphics.Point(x,610),str(YearNum)+"年")
        YearNum +=1
        YearTxt.draw(MainWin)
        x += 15
        EndPoint = graphics.Point(x,600)

        cRectangle = graphics.Rectangle(StartPoint,EndPoint)
        cRectangle.setFill("green")

        cRectangle.draw(MainWin)

        x += 5
    for i in range(10):
        pt = MainWin.getMouse()
        print("clicked x:",pt.getX(),",y:",pt.getY())

ptMoneyMap()

