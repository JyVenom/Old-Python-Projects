import turtle

xclick = 0
yclick = 0

def getcoordinates():
    turtle.onscreenclick(modifyglobalvariables) # Here's the change!

def modifyglobalvariables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print(xclick)
    print(yclick)

getcoordinates()
