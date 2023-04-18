import turtle

print ('What is the size of the board: Default size = 40')
harsha = 40
harsha = int(input())
class TicToe(object):
    def __init__(self):
        for k in range(0, harsha * 4, harsha):
            for j in range(0, harsha * 4, harsha):
                # a=turtle.pos()
                turtle.speed(100)
                turtle.ht()
                turtle.sety(j)
                turtle.setx(k)
                for i in range(4):
                    turtle.right(90)
                    turtle.forward(harsha)

                    # turtle.setx(k)
        turtle.up()
        turtle.setx(-harsha)
        turtle.sety(-harsha)
        turtle.down()
        self.ox = -harsha
        self.oy = -harsha

        turtle.ht()

    def placeX(self, x, y):
        turtle.up()
        tx = x * harsha
        ty = y * harsha
        turtle.setx(tx)
        turtle.sety(ty)
        turtle.down()
        turtle.goto(tx - harsha, ty - harsha)
        turtle.goto(tx - harsha, ty)
        turtle.goto(tx, ty - harsha)
        turtle.up()
        turtle.goto(-harsha, -harsha)
        turtle.down()
        return

 #   def placeO(self, x, y):
 #       turtle.up()
 #       tx = x * harsha
 #       ty = y * harsha
 #       turtle.goto(tx, ty)
 #       x2 = tx - harsha
 #       y2 = ty - harsha
 #       turtle.up()
 #       turtle.goto(float(tx + x2) / 2, float(ty + y2) / 2)
 #       turtle.down()
 #       turtle.dot(harsha)
 #       turtle.up()
 #       turtle.goto(-harsha, -harsha)
 #       turtle.down()
 #       return


turtle.title("Tic-Tac-Toe")
turtle.shape("arrow")
turtle.color("red", "green")
turtle.bgcolor("blue")
game = TicToe()
print('The bottom left co-ordinates are 0,0 and the top right co-ordinates are 3,3')
##game.placeO(2,2)
surender = {0: ['', '', '', ''], 1: ['', '', '', ''], 2: ['', '', '', ''], 3: ['', '', '', '']}


def victory(d, x, y):
    y = int(y)
    global case1
    global case2
    global case3
    global case4
    global case5
    global case6
    global case7
    global case8
    global case9
    global case10
    global case11
    global case12
    global diag3
    global diag4
    global diag5
    global diag6
    global diag7
    global diag8
    global row2
    global col2
    if d[x][y] == '':
        return False
    if d[x][y] == 'X':
        # print "DEBUG:X,Y in victory:",x,y
        #row = []
        row = d[x]
        #row2 = d[x]
        colum = []
        #col2 = []
        for i in d:
            colum.append(d[i][y])  # for X
            col2.append(d[i][y])  # for X
        # if x==1 and y==1:
        diag1 = [d[0][0], d[1][1], d[2][2]]
        diag2 = [d[0][2], d[1][1], d[2][0]]
        diag3 = [d[0][3], d[1][2], d[2][1]]
        diag4 = [d[1][2], d[2][1], d[3][0]]
        diag5 = [d[1][3], d[2][2], d[3][1]]
        diag6 = [d[1][1], d[2][2], d[3][3]]
        diag7 = [d[0][1], d[1][2], d[2][3]]
        diag8 = [d[1][0], d[2][1], d[3][2]]
        row1 = [row[0], row[1], row[2]]
        row2 = [row[1], row[2], row[3]]
        colum1 = [colum[0], colum[1], colum[2]]
        col2 = [colum[1], colum[2], colum[3]]

        case1 = (diag1 == ['X', 'X', 'X'])
        case2 = (diag2 == ['X', 'X', 'X'])
        case3 = (diag3 == ['X', 'X', 'X'])
        case4 = (diag4 == ['X', 'X', 'X'])
        case5 = (diag5 == ['X', 'X', 'X'])
        case6 = (diag6 == ['X', 'X', 'X'])
        case7 = (diag7 == ['X', 'X', 'X'])
        case8 = (diag8 == ['X', 'X', 'X'])
        case9 = (colum1 == ['X', 'X', 'X'])
        case10 = (col2 == ['X', 'X', 'X'])
        case11 = (row2 == ['X', 'X', 'X'])
        case12 = (row1 == ['X', 'X',  'X'])

        case1_to_case12 = (case1 or
                        case2 or
                        case3 or
                        case4 or
                        case5 or
                        case6 or
                        case7 or
                        case8 or
                        case9 or
                        case10 or
                        case11 or
                        case12)
        return case1_to_case12
        # return (('X' in row) and all(x == row[0] for x in row)) or \
        #    (('X' in row2) and all(x == row2[1] for x in row2)) or \
        #    (('X' in colum) and all(x == colum[0] for x in colum)) or \
        #    (('X' in col2) and all(x == col2[1] for x in col2)) or \
        #    (('X' in diag1) and all(x == diag1[0] for x in diag1)) or \
        #    (('X' in diag2) and all(x == diag2[0] for x in diag2)) or \
        #    (('X' in diag3) and all(x == diag3[0] for x in diag3)) or \
        #    (('X' in diag4) and all(x == diag4[0] for x in diag4)) or \
        #    (('X' in diag5) and all(x == diag5[0] for x in diag5)) or \
        #    (('X' in diag6) and all(x == diag6[0] for x in diag6)) or \
        #    (('X' in diag7) and all(x == diag7[0] for x in diag7)) or \
        #    (('X' in diag8) and all(x == diag8[0] for x in diag8))
    if d[x][y] == 'O':
        # print "DEBUG:X,Y in victory:",x,y
        row = d[x]
        colum = []
        for i in d:
            # print "DEbug string indi in victory:",i,y
            # print "Debug String in Victory:",d[i][y]
            colum.append(d[i][y])  # for O
        # if x==1 and y==1:
        diag1 = [d[0][0], d[1][1], d[2][2]]
        diag2 = [d[0][2], d[1][1], d[2][0]]
        diag3 = [d[0][3], d[1][2], d[2][1]]
        diag4 = [d[1][2], d[2][1], d[3][0]]
        diag5 = [d[1][3], d[2][2], d[3][1]]
        diag6 = [d[1][1], d[2][2], d[3][3]]
        diag7 = [d[0][1], d[1][2], d[2][3]]
        diag8 = [d[1][0], d[2][1], d[3][2]]
        row1 = [row[0], row[1], row[2]]
        row2 = [row[1], row[2], row[3]]
        colum1 = [colum[0], colum[1], colum[2]]
        col2 = [colum[1], colum[2], colum[3]]

        case13 = (diag1 == ['O', 'O', 'O'])
        case14 = (diag2 == ['O', 'O', 'O'])
        case15 = (diag3 == ['O', 'O', 'O'])
        case16 = (diag4 == ['O', 'O', 'O'])
        case17 = (diag5 == ['O', 'O', 'O'])
        case18 = (diag6 == ['O', 'O', 'O'])
        case19 = (diag7 == ['O', 'O', 'O'])
        case20 = (diag8 == ['O', 'O', 'O'])
        case21 = (col2 == ['O', 'O', 'O'])
        case22 = (colum1 == ['O', 'O', 'O'])
        case23 = (row2 == ['O', 'O', 'O'])
        case24 = (row1 == ['O', 'O', 'O'])

        case13_to_case24 = (case13 or
                            case14 or
                            case15 or
                            case16 or
                            case17 or
                            case18 or
                            case19 or
                            case20 or
                            case21 or
                            case22 or
                            case23 or
                            case24)
        return case13_to_case24
        #return (('O' in row) and all(x == row[0] for x in row)) or \
        #       (('O' in row2) and all(x == row2[1] for x in row2)) or \
        #       (('O' in colum) and all(x == colum[0] for x in colum)) or \
        #       (('O' in col2) and all(x == col2[1] for x in col2)) or \
        #       (('O' in diag1) and all(x == diag1[0] for x in diag1)) or \
        #       (('O' in diag2) and all(x == diag2[0] for x in diag2)) or \
        #       (('O' in diag3) and all(x == diag3[0] for x in diag3)) or \
        #       (('O' in diag4) and all(x == diag4[0] for x in diag4)) or \
        #       (('O' in diag5) and all(x == diag5[0] for x in diag5)) or \
        #       (('O' in diag6) and all(x == diag6[0] for x in diag6)) or \
        #       (('O' in diag7) and all(x == diag7[0] for x in diag7)) or \
        #       (('O' in diag8) and all(x == diag8[0] for x in diag8))


def win(d, v):
    # print "This is d:",d
    c = d.copy()
    # print c
    for i in range(3):
        for j in range(3):
            if c[i][j] == '':
                c[i][j] = v
                # print "DEBUG: WIN:",i,j
                if victory(c, i, j) == True:
                    return (i, j, True)
                else:
                    c[i][j] = ''
                    continue

            else:
                continue
    return (0, 0, False)


# import math
def getopp(d, x, y):
    if d[abs(2 - x)][abs(2 - y)] == '':
        return (abs(2 - x), abs(2 - y), True)
    else:
        return (0, 0, False)


def drawg(d):
    l = []
    for i in d:
        for j in range(3):
            l.append(d[i][j])
    return '' in l


def chkcorner(d):
    if d[2][2] == '':
        return (2, 2, True)
    if d[0][0] == '':
        return (0, 0, True)
    if d[2][0] == '':
        return (2, 0, True)
    if d[0][2] == '':
        return (0, 2, True)
    return (0, 0, False)


print (
"Welcome, This is a game of Tic-Tac-Toe with improved Graphics over the C++ version, Created by Surender Harsha:\n1.Player Start")
print ("2.Computer Start")
n = int(input())
if n == 1:
    print ('You are X , computer is O')
    while 1:
        # print d

        if drawg(surender) == False:
            print ('Its a draw')
            break
        print ('Click the box you wish to put X on:')
        x = int(1)
        y = int(1)
        turtle.onscreenclick(x, y)
        if x >= -1 and x <= 0.5:
            x=0
        if x >= 1 and x <= 1.5:
            x=1
        if x >= 2 and x <= 2.5:
            x=2
        if x >= 3 and x <= 4:
            x=3
        if y >= -1 and y <= 0.5:
            y=0
        if y >= 1 and y <= 1.5:
            y=1
        if y >= 2 and y <= 2.5:
            y=2
        if y >= 3 and y <= 4:
            y=3
        x = int(x)
        y = int(y)
        if surender[x][y] != '':
            print ('The Position you have entered is invalid,Please enter again')
            continue
        game.placeX(y, x)
        surender[x][y] = 'X'

        if victory(surender, x, y):
            print ('Congratulations! You have won!')
            break
        k = win(surender, 'O')
        if k[2] == True:
            surender[k[0]][k[1]] = 'O'
            game.placeO(k[1], k[0])

            print ('Computer has won!')
            break
        k = win(surender, 'X')
        # print k
        if k[2] == True:
            surender[k[0]][k[1]] = 'O'
            game.placeO(k[1], k[0])
            continue
        flag = 0
        if x == 1 and y == 1:
            if surender[0][0] == '':
                surender[0][0] = 'O'
                game.placeO(0, 0)
                continue
            if surender[2][2] == '':
                surender[2][2] = 'O'
                game.placeO(2, 2)
                continue
            if surender[2][0] == '':
                surender[2][0] = 'O'
                game.placeO(0, 2)
                continue
            if surender[0][2] == '':
                surender[0][2] = 'O'
                game.placeO(2, 0)
                continue
            for i in range(3):
                for j in range(3):
                    if surender[i][j] == '':
                        surender[i][j] = 'O'
                        game.placeO(j, i)
                        flag = 1
                        break
                if flag == 1:
                    break
        else:
            l = getopp(surender, x, y)
            if l[2] == True:
                surender[l[0]][l[1]] = 'O'
                game.placeO(l[1], l[0])
                continue
            else:
                flag = 0
                for i in range(3):
                    for j in range(3):
                        if surender[i][j] == '':
                            surender[i][j] = 'O'
                            game.placeO(j, i)
                            flag = 1
                            break
                    if flag == 1:
                        break

else:
    print ('you are X, computer is O')
    while 1:
        if drawg(surender) == False:
            print ('Its a draw')
            break
        AI = 0
        k = win(surender, 'O')
        if k[2] == True:
            surender[k[0]][k[1]] = 'O'
            game.placeO(k[1], k[0])

            print ('Computer has won!')
            turtle.bye()
            import sys

            sys.exit()
        k = win(surender, 'X')
        # print k
        if k[2] == True:
            surender[k[0]][k[1]] = 'O'
            game.placeO(k[1], k[0])
            AI = 1
        if AI == 0:
            k = chkcorner(surender)
            if k[2] == True:
                surender[k[0]][k[1]] = 'O'
                game.placeO(k[1], k[0])
                AI = 1
        if AI == 0:
            if surender[1][1] == '':
                surender[1][1] = 'O'
                game.placeO(1, 1)
                AI = 1
        if AI == 0:
            flag = 0
            for i in range(3):
                for j in range(3):
                    if surender[i][j] == '':
                        surender[i][j] = 'O'
                        game.placeO(j, i)
                        flag = 1
                        break
                if flag == 1:
                    break
            AI = 1
        # Player Turn
        if drawg(surender) == False:
            print ('Its a draw')
            break
        while 1:
            x, y = raw_input('Enter The co-ordinates of X:').split()
            x = int(x)
            y = int(y)
            if surender[x][y] != '':
                print ('Please Enter Valid Co-ordinates')
                continue
            else:
                break

        surender[x][y] = 'X'
        game.placeX(y, x)
        if victory(surender, x, y) == True:
            print ('Congratulations You have won this game!')
            break
        if drawg(surender) == False:
            print ('Its a draw')
            break

turtle.bye()
