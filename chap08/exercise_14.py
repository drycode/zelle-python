#This program converts a color image to grayscale
from graphics import *

def fileWindow(infile, wWidth, wHeight):
    win = GraphWin("Original", wWidth, wHeight)
    #win.setCoords(-10, -10, 10, 10)
    infile.draw(win)
    #win.getMouse()

    height = 1
    while height < wHeight:
        for i in range (wWidth - 1):
            #r, g, b = get pixel info for current row and column
            r, g, b = infile.getPixel(i + 1, height)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            #set pixel to color_rgb(brightness, brightness, brightness)
            infile.setPixel((i + 1), (height), color_rgb(brightness, brightness, brightness))
        #update the image # to see progress row by row

        win.update()
        height = height + 1

    return win


#Get file from user
def main():
    fname = input("Enter a filename to be converted: ")
    infile = Image(Point(0,0), fname)

    wWidth = infile.getWidth()
    wHeight = infile.getHeight()
    infile = Image(Point(wWidth/2, wHeight/2), fname)
    win = fileWindow(infile, wWidth, wHeight)
    outfileName = input("Where should we save the updated file: ")
    infile.save(outfileName)



#userfile.py chapt 5
main()
