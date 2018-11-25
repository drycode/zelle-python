from graphics import *

def main():
    #Introduction
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400.0)
    #Draw interface
    Text(Point(1,8000), "Initial Principal:").draw(win)
    Text(Point(1,6000), "Interest Rate:").draw(win)
    input1 = Entry(Point(5,8000), 5)
    input1.setText("0")
    input1.draw(win)
    input2 = Entry(Point(5,6000), 5)
    input2.setText("0")
    input2.draw(win)

    output = Text(Point(2,1), "")
    output.draw(win)
    button = Text(Point(5,3750), "Graph It")
    button.draw(win)
    Rectangle(Point(4,3000), Point(6,4500)).draw(win)

    #Pause for user input
    win.getMouse()
    win.close()

    #Get principal and interest rate
    principal = eval(input1.getText())
    apr = eval(input2.getText())


    #Create a graphics window with labels on the left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400.0)

    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    #Draw bar for intial principal
    height = principal * 0.02
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)


    for year in range (1,11):
        #Calculate value for the next year
        principal = principal * (1 + .01 * apr)
        #draw bar for this value
        x11 = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("Green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close()

main()
