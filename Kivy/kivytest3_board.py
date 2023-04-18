from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


SYMBOLS = ('X', 'O')


def symbol_generator():
    while True:
        for symbol in SYMBOLS:
            yield symbol


class Board(GridLayout):

    #grid = None
    #symbols = None

    def __init__(self, cols=4, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.cols = cols
        self.rows = cols
        self.symbols = symbol_generator()

        self.grid = [[None for col in range(self.cols)] for row in range(self.rows)]

        self.surender = {0: ['', '', '', ''], 1: ['', '', '', ''], 2: ['', '', '', ''], 3: ['', '', '', '']}

        self._draw_tiles()

        #self.whogoesfirst()

    def _draw_tiles(self):
        """
            Adds the tiles to the grid (widgets to the gridset)
        """
        for row in range(self.rows):
            for col in range(self.cols):
                tile = Button()
                tile.bind(on_release=self.placeX)
                self.grid[row][col] = tile
                self.add_widget(tile)

    def whogoesfirst(self):
        Player_Start = Button(text='I Start')
        Computer_Start = Button(text='You Start')
        content = BoxLayout(orientation='vertical')
        content.add_widget(Computer_Start)
        content.add_widget(Player_Start)

        popup = Popup(title='Who Goes First?',
                      content=content,
                      size_hint=(.8, .8)).open()

        Player_Start.bind(on_release=popup.dismiss)
        Computer_Start.bind(on_release=popup.dismiss)

        Player_Start.bind(on_release=self.placeX)
        Computer_Start.bind(on_release=self.AI)

    def placeX(self, instance):
        """
            Handles a click on a tile
        """
        if instance.text:
            close_button = Button(text='Close')

            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='This square is invalid, please choose another square'))
            content.add_widget(close_button)

            popup = Popup(title='Error',
                          content=content,
                          size_hint=(.8, .8)).open()

            close_button.bind(on_release=popup.dismiss)

        instance.text = self.symbols.next()

        #self.AI()

        self._check_status()

    def placeO(self, col, row):
        self._check_status()

    def AI(self):
        for t in range(0,1):
            surender = self.surender
            k = self.win(surender, 'O')
            if k[2] == True:  # if "O" can win, put "O" there
                surender[k[1]][k[0]] = 'O'  # surender(row, col)

                self.placeO(k[0], k[1])

                self._check_status()
                while 1:
                    pass
            k = self.win(surender, 'X')  # find if there is a space where x can win and where
            # print k
            if k[2] == True:  # if there is a winning position for x, put "O" on that position
                surender[k[1]][k[0]] = 'O'
                self.placeO(k[0], k[1])
                continue
            k = self.ultimatewin(surender, 'O')  # computer 012
            # k[0]:col      k[1]:row        k[2]:101
            if k[2]:
                surender[k[1]][k[0]] = 'O'
                self.placeO(k[0], k[1])  # place0(col, row)
                continue

            k = self.ultimatewin(surender, 'X')  # player 012
            if k[2]:
                surender[k[1]][k[0]] = 'O'
                self.placeO(k[0], k[1])
                continue

            if surender[1][1] == '':
                surender[1][1] = 'O'
                self.placeO(1, 1)
                continue
            elif surender[2][2] == '':
                surender[2][2] = 'O'
                self.placeO(2, 2)
                continue
            elif surender[2][1] == '':
                surender[2][1] = 'O'
                self.placeO(1, 2)
                continue
            elif surender[1][2] == '':
                surender[1][2] = 'O'
                self.placeO(2, 1)
                continue
            else:
                l = self.getopp(surender)
                if l[2]:
                    surender[l[0]][l[1]] = 'O'
                    self.placeO(l[1], l[0])
                    continue
                else:
                    flag = 0
                    for i in range(4):
                        for j in range(4):
                            if surender[i][j] == '':
                                surender[i][j] = 'O'
                                self.placeO(j, i)
                                flag = 1
                                break
                        if flag == 1:
                            break

    def _check_status(self):
        """
            Checks board status
        """
        winner = self._get_winner()

        if winner:
            restart_button = Button(text='Restart')
            end_button = Button(text='Quit')

            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text='%s won the game!' % winner))
            content.add_widget(restart_button)
            content.add_widget(end_button)

            popup = Popup(title='%s won!' % winner,
                                content=content,
                                size_hint=(.8, .8)).open()

            restart_button.bind(on_release=popup.dismiss)
            end_button.bind(on_release=popup.dismiss)
            end_button.bind(on_release=self.exit1)

            self._restart_board()

        tie = self.Tie()

        if tie:
            restart_button = Button(text='Restart')
            end_button = Button(text='Quit')

            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text="It's a tie!"))
            content.add_widget(restart_button)
            content.add_widget(end_button)

            popup = Popup(title='Tie',
                          content=content,
                          size_hint=(.8, .8)).open()

            restart_button.bind(on_release=popup.dismiss)
            end_button.bind(on_release=popup.dismiss)
            end_button.bind(on_release=self.exit1)

            self._restart_board()

    def _get_winner(self):
        """
            Returns winning symbol or None
        """
        values = [[col.text for col in row] for row in self.grid]

        # check horizontal
        for row in values:
            result = self._is_same_symbol(row)
            if result:
                return result

        # check vertical
        for row in [list(row) for row in zip(*values)]:
            row1 = row
            result = self._is_same_symbol(row)
            if result:
                return result

        # check forward diagonal
        forward_diagonal = [row[col] for col, row in enumerate(values)]
        result = self._is_same_symbol(forward_diagonal)
        if result:
            return result

        # check backwards diagonal
        backwards_diagonal = [row[-col-1] for col, row in enumerate(values)]
        result = self._is_same_symbol(backwards_diagonal)
        if result:
            return result

        return None

    def _is_same_symbol(self, row):
        for x in range (2):
            row_1 = row
            if x == 0:
                row = row[:3]
            if x == 1:
                row = row[1:]
            for symbol in SYMBOLS:
                if [symbol for _ in range(3)] == row:
                    return symbol
            row = row_1
        return False

    def Tie(self):
        values = [[col.text for col in row] for row in self.grid]

        for x in range(0,3):
            for y in range(0,3):
                if values[x][y] == '':
                    return None
        return True

    def exit1(self):
        exit(0)

    def win(self,d, v):
        # print "This is d:",d
        c = d
        # print c
        for i in range(4):
            for j in range(4):
                if c[i][j] == '':
                    c[i][j] = v
                    # print "DEBUG: WIN:",i,j
                    if self.victory2(c, i, j) == True:
                        return (j, i, True)
                    else:
                        c[i][j] = ''
                        continue

                else:
                    continue
        return (0, 0, False)

    def victory(self,d, x, y):
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
        global row1
        global row2
        global column
        global col2
        if d[y][x] == '':
            return False
        if d[y][x] == 'X':
            # print "DEBUG:X,Y in victory:",x,y
            # row = []
            row = d[y]
            column = []
            for i in d:
                column.append(d[i][x])  # for X
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
            column1 = [column[0], column[1], column[2]]
            col2 = [column[1], column[2], column[3]]

            case1 = (diag1 == ['X', 'X', 'X'])
            case2 = (diag2 == ['X', 'X', 'X'])
            case3 = (diag3 == ['X', 'X', 'X'])
            case4 = (diag4 == ['X', 'X', 'X'])
            case5 = (diag5 == ['X', 'X', 'X'])
            case6 = (diag6 == ['X', 'X', 'X'])
            case7 = (diag7 == ['X', 'X', 'X'])
            case8 = (diag8 == ['X', 'X', 'X'])
            case9 = (column1 == ['X', 'X', 'X'])
            case10 = (col2 == ['X', 'X', 'X'])
            case11 = (row2 == ['X', 'X', 'X'])
            case12 = (row1 == ['X', 'X', 'X'])

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
        if d[y][x] == 'O':
            # print "DEBUG:X,Y in victory:",x,y
            row = d[y]
            column = []
            for i in d:
                # print "DEbug string indi in victory:",i,y
                # print "Debug String in Victory:",d[i][y]
                column.append(d[i][y])  # for O
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
            column1 = [column[0], column[1], column[2]]
            col2 = [column[1], column[2], column[3]]

            case13 = (diag1 == ['O', 'O', 'O'])
            case14 = (diag2 == ['O', 'O', 'O'])
            case15 = (diag3 == ['O', 'O', 'O'])
            case16 = (diag4 == ['O', 'O', 'O'])
            case17 = (diag5 == ['O', 'O', 'O'])
            case18 = (diag6 == ['O', 'O', 'O'])
            case19 = (diag7 == ['O', 'O', 'O'])
            case20 = (diag8 == ['O', 'O', 'O'])
            case21 = (col2 == ['O', 'O', 'O'])
            case22 = (column1 == ['O', 'O', 'O'])
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
            # return (('O' in row) and all(x == row[0] for x in row)) or \
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

    def victory2(self,d, x, y):
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
        global row1
        global row2
        global column
        global col2
        if d[x][y] == '':
            return False
        if d[x][y] == 'X':
            # print "DEBUG:X,Y in victory:",x,y
            # row = []
            row = d[x]
            column = []
            for i in d:
                column.append(d[i][y])  # for X
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
            column1 = [column[0], column[1], column[2]]
            col2 = [column[1], column[2], column[3]]

            case1 = (diag1 == ['X', 'X', 'X'])
            case2 = (diag2 == ['X', 'X', 'X'])
            case3 = (diag3 == ['X', 'X', 'X'])
            case4 = (diag4 == ['X', 'X', 'X'])
            case5 = (diag5 == ['X', 'X', 'X'])
            case6 = (diag6 == ['X', 'X', 'X'])
            case7 = (diag7 == ['X', 'X', 'X'])
            case8 = (diag8 == ['X', 'X', 'X'])
            case9 = (column1 == ['X', 'X', 'X'])
            case10 = (col2 == ['X', 'X', 'X'])
            case11 = (row2 == ['X', 'X', 'X'])
            case12 = (row1 == ['X', 'X', 'X'])

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
            column = []
            for i in d:
                # print "DEbug string indi in victory:",i,y
                # print "Debug String in Victory:",d[i][y]
                column.append(d[i][y])  # for O
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
            column1 = [column[0], column[1], column[2]]
            col2 = [column[1], column[2], column[3]]

            case13 = (diag1 == ['O', 'O', 'O'])
            case14 = (diag2 == ['O', 'O', 'O'])
            case15 = (diag3 == ['O', 'O', 'O'])
            case16 = (diag4 == ['O', 'O', 'O'])
            case17 = (diag5 == ['O', 'O', 'O'])
            case18 = (diag6 == ['O', 'O', 'O'])
            case19 = (diag7 == ['O', 'O', 'O'])
            case20 = (diag8 == ['O', 'O', 'O'])
            case21 = (col2 == ['O', 'O', 'O'])
            case22 = (column1 == ['O', 'O', 'O'])
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
            # return (('O' in row) and all(x == row[0] for x in row)) or \
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

    def ultimatewin(self,g, c):
        # g:surender, c:find 101 for
        # return(col, row, 101)

        global row1
        global row2
        global row3
        global row4
        global col1
        global col2
        global col3
        global col4
        global diag1
        global diag2
        row1 = g[0]
        row2 = g[1]
        row3 = g[2]
        row4 = g[3]
        col1 = []
        col2 = []
        col3 = []
        col4 = []
        diag1 = [g[0][0], g[1][1], g[2][2], g[3][3]]
        diag2 = [g[3][0], g[2][1], g[1][2], g[0][3]]
        for i in g:
            col1.append(g[i][0])
        for i in g:
            col2.append(g[i][1])
        for i in g:
            col3.append(g[i][2])
        for i in g:
            col4.append(g[i][3])
        if diag1 == ['', c, '', '']:
            return (2, 2, True)  # return(col, row, 101)
        if diag2 == ['', c, '', '']:
            return (2, 1, True)
        if row1 == ['', c, '', '']:
            return (2, 0, True)
        if row2 == ['', c, '', '']:
            return (2, 1, True)
        if row3 == ['', c, '', '']:
            return (2, 2, True)
        if row4 == ['', c, '', '']:
            return (2, 3, True)
        if col1 == ['', c, '', '']:
            return (0, 2, True)
        if col2 == ['', c, '', '']:
            return (1, 2, True)
        if col3 == ['', c, '', '']:
            return (2, 2, True)
        if col4 == ['', c, '', '']:
            return (3, 2, True)
        if diag1 == ['', '', c,
                     '']:  ############################################################################################
            return (1, 1, True)
        if diag2 == ['', '', c, '']:
            return (1, 2, True)
        if row1 == ['', '', c, '']:
            return (1, 0, True)
        if row2 == ['', '', c, '']:
            return (1, 1, True)
        if row3 == ['', '', c, '']:
            return (1, 2, True)
        if row4 == ['', '', c, '']:
            return (1, 3, True)
        if col1 == ['', '', c, '']:
            return (0, 1, True)
        if col2 == ['', '', c, '']:
            return (1, 1, True)
        if col3 == ['', '', c, '']:
            return (2, 1, True)
        if col4 == ['', '', c, '']:
            return (3, 1, True)
        else:
            return (0, 0, False)

    def getopp(self,d, x, y):
        if d[abs(2 - x)][abs(2 - y)] == '':
            return (abs(2 - x), abs(2 - y), True)
        else:
            return (0, 0, False)

    def _restart_board(self):
        for row in self.grid:
            for col in row:
                col.text = ''
        self.surender = {0: ['', '', '', ''], 1: ['', '', '', ''], 2: ['', '', '', ''], 3: ['', '', '', '']}