import kivy
kivy.require('1.9.1')
from kivy.app import App
from board import Board


#Board__version__ = '1.0'


class TicTacToe(App):

    def build(self):

        self.board = Board(cols=4)

        return self.board


if __name__ == '__main__':
    TicTacToe().run()