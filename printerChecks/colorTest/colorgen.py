import colorsys
import random
import time
import htmlcolors
import Queue
import math

colCount = 80
rowCount = 63

def colorsineBW1D():
    for i in range(0,rowCount):
        buffer.append([])
        for j in rnage(0, colCount):
            buffer[i].append(0)
            

def justRandom():
    random.seed(time.clock())
	
    buffer = []
    color = 0
    x = 0
    y = 0
    cont = True
    coord = ()

    pix = []

    for i in range(0,rowCount):
        buffer.append([])
        for j in range(0,colCount):
            buffer[i].append((0,0,0))

    for i in range(0,100000):
        r = random.randrange(0,255,1)
        g = random.randrange(0,255,1)
        b = random.randrange(0,255,1)
        x = random.randrange(0,rowCount-1,1)
        y = random.randrange(0,colCount-1,1)
	
        buffer[x][y] = [r, g, b]
        
        stuffqueue(buffer, pix, x, y)
        
	while len(pix) > 0:
            coord = pix.pop()
            buffer[coord[0]][coord[1]] = [r, g, b]
            stuffqueue(buffer, pix, coord[0], coord[1])

    dumpHTML(buffer)

def randomSplashes():
    random.seed(time.clock())
	
    buffer = []
    color = 0
    x = 0
    y = 0
    cont = True
    coord = ()

    pix = []

    for i in range(0,rowCount):
        buffer.append([])
        for j in range(0,colCount):
            buffer[i].append(color)

    for i in range(0,1000):
        color = random.randrange(0,26,1)
        x = random.randrange(0,rowCount-1,1)
        y = random.randrange(0,colCount-1,1)
	
        buffer[x][y] = color
       
        pix = [] 
        stuffqueue(buffer, pix, x, y)
        
	while len(pix) > 0:
            coord = pix.pop()
            buffer[coord[1]][coord[0]] = color
            stuffqueue(buffer, pix, coord[0], coord[1])

    dumpHTML(buffer, 1)

def stuffqueue(buffer, pix, x, y):
    if buffer[x-1][y] != 0:
        temp = (x-1, y)
        if pix.count(temp):
            print "yes"
            pix.append( (x-1, y) )

    if buffer[x+1][y] != 0:
        temp = (x+1, y)
        if pix.count(temp):
            print "yes"
            pix.append( (x+1, y) )

    if buffer[x][y-1] != 0:
        temp = (x, y-1)
        if pix.count(temp):
            print "yes"
            pix.append( (x, y-1) ) 

    if buffer[x][y+1] != 0:
        temp = (x, y+1)
        if pix.count(temp):
            print "yes"
            pix.append( (x, y+1) )
 
    return pix

def dumpHTML(buffer, mode=0):
    f = open("./colortest.html", 'w')
    f.write("<html><body style=\"background-color:black\">")
    k = 0
    l = 0

    for i in buffer:
        for j in i:
            if mode == 0:
                f.write("<font color=\"" + rgbToHex(j) + "\">A</font>")
            if mode == 1:
                f.write("<font color=\"" + htmlcolors.htcol[j] + "\">A</font>")
            l += 1
        k += 1
        f.write("<br/>")

    

    f.write("</body></html>")

def rgbToHex(rgb):
    hexr = hex(rgb[0])[2:]
    hexg = hex(rgb[1])[2:]
    hexb = hex(rgb[2])[2:]
   
    if len(hexr) < 2:
        hexr = "0" + hexr  
    if len(hexg) < 2:
        hexg = "0" + hexg
    if len(hexb) < 2:
        hexb = "0" + hexb

    return "#" + hexr + hexg + hexb
    

if __name__=="__main__":
    justRandom()
    print
    print rgbToHex((255,0,255))
