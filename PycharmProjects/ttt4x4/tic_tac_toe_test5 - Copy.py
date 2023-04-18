import turtle



#I need to fix the positions of the X and O's so that they draw more perfectly into the        squares of the board.



class TicTacToe:
    def __init__(self):
        self.u__init_board = []

    def draw_board():
        '''draws a tic-tac-toe board over the 9 turtle squares'''
        t=turtle.Turtle()
        t.ht() # makes the turtle invisible
        t.speed(10000)
        t.up()
        t.goto(-40,-40)
        t.down()
        t.forward(240)
        t.left(90)
        t.forward(240)
        t.left(90)
        t.forward(240)
        t.left(90)
        t.forward(80)
        t.left(90)
        t.forward(240)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(240)
        t.left(90)
        t.goto(-40,-40)
        t.left(180)
        t.forward(160)
        t.up()
        t.goto(40,-40)
        t.down()
        t.forward(240)
        t.right(90)
        t.forward(80)
        t.right(90)
        t.forward(240)

    def setup_board():
        '''Creates 3 rows of 3 turtles using range(0, 240, 80); turtle.Turtle(); up(); shape('square'); shapesize(4, 4, 4);
        color('white'); goto(x, y). Each turtle is registered to respond to click events using onclick(mark).
        Calls draw_grid() once the 9 turtles are on the board.'''
        for y in range(0,240,80):
            for x in range (0,240,80):
             t=turtle.Turtle()
             t.up()
             t.shape('square')
             t.shapesize(4,4,4,)
             t.color('white')
             t.goto(x,y)
             t.onclick(TicTacToe.mark)
        TicTacToe.draw_board()

    def mark(x, y):

        '''Function is invoked whenever a turtle registered to respond to click event is clicked. Creates a turtle and draws
        either a circle or an x centered on the x, y coordinates of the click.
        Be sure to set circle to False once the circle is drawn and to True once the x is drawn. '''
        ct = turtle.Turtle()
        ct.ht() #hides the turtle (makes the turtle invisable)
        ct.up()
        if x >= -39 and x<= 40:
            x=1
        if x >= 41 and x<= 120:
            x=81
        if x >= 121 and x<= 200:
            x=161
        if y >= -39 and y<= 40:
            y=1
        if y >= 41 and y<= 120:
            y=81
        if y >= 121 and y<= 200:
            y=161
        global circle
        if circle:
            turtle.penup()
            #turtle.speed(0)
            turtle.goto(x,y)
            turtle.down()
            turtle.dot(69)
            turtle.dot(67, "white")
            turtle.left(45)
            circle = False
        else:
            turtle.up()
            #turtle.speed(0)
            turtle.goto(x,y)
            turtle.down()
            turtle.left(45)
            turtle.forward(40)
            turtle.left(180)
            turtle.forward(80)
            turtle.left(180)
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(40)
            turtle.left(180)
            turtle.forward(80)
            circle = True



    def main():
        wn = turtle.Screen()
        wn.title('OG Tic Tac Toe')
        wn.bgcolor("red")
        global circle
        circle = False
        TicTacToe.setup_board()
        return 'Done'


if __name__ == '__main__':
    TicTacToe.main()
    turtle.TK.mainloop()
