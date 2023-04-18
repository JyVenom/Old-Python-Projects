import turtle
print 'What is the size of the board: Default size = 40'
harsha=40
harsha=int(raw_input())
class TicToe(object):
    def __init__(self):
        for k in range(0,harsha*3,harsha):
            for j in range(0,harsha*3,harsha):
            #a=turtle.pos()
                turtle.sety(j)
                turtle.setx(k)
                for i in range(4):
                    turtle.right(90)
                    turtle.forward(harsha)
                
            #turtle.setx(k)
        turtle.up()
        turtle.setx(-harsha)
        turtle.sety(-harsha)
        turtle.down()
        self.ox=-harsha
        self.oy=-harsha
    

    def placeX(self,x,y):
        turtle.up()
        tx=x*harsha
        ty=y*harsha
        turtle.setx(tx)
        turtle.sety(ty)
        turtle.down()
        turtle.goto(tx-harsha,ty-harsha)
        turtle.goto(tx-harsha,ty)
        turtle.goto(tx,ty-harsha)
        turtle.up()
        turtle.goto(-harsha,-harsha)
        turtle.down()
        return
    def placeO(self,x,y):
        turtle.up()
        tx=x*harsha
        ty=y*harsha
        turtle.goto(tx,ty)
        x2=tx-harsha
        y2=ty-harsha
        turtle.up()
        turtle.goto(float(tx+x2)/2,float(ty+y2)/2)
        turtle.down()
        turtle.dot(harsha)
        turtle.up()
        turtle.goto(-harsha,-harsha)
        turtle.down()
        return
turtle.title("Tic-Tac-Toe")
turtle.shape("arrow")
turtle.color("red", "green")
turtle.bgcolor("blue")        
game=TicToe()
print 'The bottom left co-ordinates are 0,0 and the top right co-ordinates are 2,2'
##game.placeO(2,2)
surender={0:['','',''],1:['','',''],2:['','','']}
def victory(d,x,y):
    y=int(y)
    if d[x][y]=='':
        return False
    if d[x][y]=='X':
        #print "DEBUG:X,Y in victory:",x,y
        row=d[x]
        colum=[]
        for i in d:
            colum.append(d[i][y])#for X
        diag1=[]
        diag2=[]
        if x==1 and y==1:
            diag1=[d[0][0],d[1][1],d[2][2]]
            diag2=[d[0][2],d[1][1],d[2][0]]
        return (('X' in row) and all(x==row[0] for x in row)) or (('X' in colum) and all(x==colum[0] for x in colum)) or (('X' in diag1) and all(x==diag1[0] for x in diag1)) or (('X' in diag2) and all(x==diag2[0] for x in diag2))
    if d[x][y]=='O':
        #print "DEBUG:X,Y in victory:",x,y
        row=d[x]
        colum=[]
        for i in d:
            #print "DEbug string indi in victory:",i,y
            #print "Debug String in Victory:",d[i][y]
            colum.append(d[i][y])#for O
        diag1=[]
        diag2=[]
        if x==1 and y==1:
            diag1=[d[0][0],d[1][1],d[2][2]]
            diag2=[d[0][2],d[1][1],d[2][0]]
        return (('O' in row) and all(x==row[0] for x in row)) or (('O' in colum) and all(x==colum[0] for x in colum)) or (('O' in diag1) and all(x==diag1[0] for x in diag1)) or (('O' in diag2) and all(x==diag2[0] for x in diag2)) 
        
def win(d,v):
    #print "This is d:",d
    c=d.copy()
    #print c
    for i in range(3):
        for j in range(3):
            if c[i][j]=='':
                c[i][j]=v
                #print "DEBUG: WIN:",i,j
                if victory(c,i,j)==True:
                    return (i,j,True)
                else:
                    c[i][j]=''
                    continue
                
            else:
                 continue   
    return (0,0,False)
#import math               
def getopp(d,x,y):
      if d[abs(2-x)][abs(2-y)]=='':
          return (abs(2-x),abs(2-y),True)
      else:
          return (0,0,False)            
                
def drawg(d):
    l=[]
    for i in d:
         for j in range(3):
             l.append(d[i][j])
    return '' in l  
def chkcorner(d):
    if d[2][2]=='':
        return (2,2,True)
    if d[0][0]=='':
        return (0,0,True)
    if d[2][0]=='':
        return (2,0,True)
    if d[0][2]=='':
        return (0,2,True)
    return (0,0,False)     
print "Welcome, This is a game of Tic-Tac-Toe with improved Graphics over the C++ version, Created by Surender Harsha:\n1.Player Start"
print "2.Computer Start"
n=int(raw_input())
if n==1:
 print 'You are X , computer is O'
 while 1:
    #print d
    
    if drawg(surender)==False:
        print 'Its a draw'
        break
    print 'Enter the co-ordinates you wish to put X on:'
    x,y=raw_input().split()
    x=int(x)
    y=int(y)
    if surender[x][y]!='':
        print 'The Position you have entered is invalid,Please enter again'
        continue
    game.placeX(y,x)
    surender[x][y]='X'
    
    if victory(surender,x,y):
        print 'Congratulations! You have won!'
        break
    k=win(surender,'O')
    if k[2]==True:
        
            surender[k[0]][k[1]]='O'
            game.placeO(k[1],k[0])
        
            print 'Computer has won!'
            break
    k=win(surender,'X')
    #print k
    if k[2]==True:
        
            surender[k[0]][k[1]]='O'
            game.placeO(k[1],k[0])
            continue
    flag=0
    if x==1 and y==1:
        if surender[0][0]=='':
            surender[0][0]='O'
            game.placeO(0,0)
            continue
        if surender[2][2]=='':
            surender[2][2]='O'
            game.placeO(2,2)
            continue
        if surender[2][0]=='':
            surender[2][0]='O'
            game.placeO(0,2)
            continue
        if surender[0][2]=='':
            surender[0][2]='O'
            game.placeO(2,0)
            continue
        for i in range(3):
            for j in range(3):
                if surender[i][j]=='':
                    surender[i][j]='O'
                    game.placeO(j,i)
                    flag=1
                    break
            if flag==1:
                break
    else:
        l=getopp(surender,x,y)
        if l[2]==True:
            surender[l[0]][l[1]]='O'
            game.placeO(l[1],l[0])
            continue
        else:
            flag=0
            for i in range(3):
                for j in range(3):
                    if surender[i][j]=='':
                        surender[i][j]='O'
                        game.placeO(j,i)
                        flag=1
                        break
                if flag==1:
                    break
            
else:
    print 'you are X, computer is O'
    while 1:
         if drawg(surender)==False:
            print 'Its a draw'
            break
         AI=0
         k=win(surender,'O')
         if k[2]==True:
        
            surender[k[0]][k[1]]='O'
            game.placeO(k[1],k[0])
        
            print 'Computer has won!'
            turtle.bye()
            import sys
            sys.exit()
         k=win(surender,'X')
         #print k
         if k[2]==True:
        
            surender[k[0]][k[1]]='O'
            game.placeO(k[1],k[0])
            AI=1
         if AI==0:
          k=chkcorner(surender)
          if k[2]==True:
             surender[k[0]][k[1]]='O'
             game.placeO(k[1],k[0])
             AI=1
         if AI==0:
             if surender[1][1]=='':
                 surender[1][1]='O'
                 game.placeO(1,1)
                 AI=1
         if AI==0:
            flag=0
            for i in range(3):
                for j in range(3):
                    if surender[i][j]=='':
                        surender[i][j]='O'
                        game.placeO(j,i)
                        flag=1
                        break
                if flag==1:
                    break
            AI=1
         #Player Turn
         if drawg(surender)==False:
            print 'Its a draw'
            break
         while 1:
            x,y=raw_input('Enter The co-ordinates of X:').split()
            x=int(x)
            y=int(y)
            if surender[x][y]!='':
                print 'Please Enter Valid Co-ordinates'
                continue
            else:
                break
         surender[x][y]='X'
         game.placeX(y,x)
         if victory(surender,x,y)==True:
             print 'Congratulations You have won this game!'
             break
         if drawg(surender)==False:
            print 'Its a draw'
            break
           
turtle.bye()        
