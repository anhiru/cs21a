# ----------------------------------------------------------------------------
# Name:         eztictac
# Purpose:      implement a game of Tic Tac Toe
#
# Author:       Andrew Tran
# Date:         06/16/2019
# ----------------------------------------------------------------------------
"""
Module to implement a GUI for a game of Tic Tac Toe
"""

import tkinter
import random


class Game(object):
    """
    GUI Game class to support a game of Tic Tac Toe

    Arguments:
    parent: the root window object (tkinter.Tk)

    Attributes:
    canvas: the canvas representing the game self.board (tkinter.Canvas)
    outcome_message: the label to display outcome of the game (tkinter.Label)
    """

    TILE_SIZE = 100  # constant length/width of each tile
    board = [[None for i in range(3)] for j in range(3)]  # 2D grid of board
    moves = 0  # 9 total moves possible on a 3x3 grid

    def __init__(self, parent):
        parent.title('Tic Tac Toe')

        # create a RESTART button and associate it with the restart method
        restart_button = tkinter.Button(parent, text='RESTART',
                                        width=10, command=self.restart)
        # register it with the grid() geometry manager
        restart_button.grid()

        # create a canvas to draw our board
        self.canvas = tkinter.Canvas(parent,
                                     width=self.TILE_SIZE*3,
                                     height=self.TILE_SIZE*3)
        # register it with the grid() geometry manager
        self.canvas.grid()

        # draw the tiles on the canvas
        for row in range(3):
            for column in range(3):
                self.canvas.create_rectangle(self.TILE_SIZE * column,
                                             self.TILE_SIZE * row,
                                             self.TILE_SIZE * (column + 1),
                                             self.TILE_SIZE * (row + 1),
                                             fill='#ffffff')

        # bind left clicks on the canvas to the play method
        self.canvas.bind('<Button-1>', self.play)

        # create a label for the win/lose/tie message
        self.outcome_message = tkinter.Label(parent, text='')
        # register it with the grid() geometry manager
        self.outcome_message.grid()

    def restart(self):
        """
        Invoked when the user clicks on the restart button, restarts the game

        :return: None
        """
        # clear game board
        self.board = [[None for i in range(3)] for j in range(3)]

        # revert all squares to white
        for square in self.canvas.find_all():
            self.canvas.itemconfigure(square, fill='#ffffff')

        # rebind left click to self.play
        self.canvas.bind('<Button-1>', self.play)

        # clear outcome message
        self.outcome_message.config(text='')

        # reinitialize moves to zero
        self.moves = 0

    def play(self, event):
        """
        Invoked when the user clicks on a square, dictates flow of the game

        :param event: event object giving access to click coordinates (Event)
        :return: None
        """
        # user's turn
        row = (event.y // self.TILE_SIZE)  # y-coord of row in 2D grid
        column = (event.x // self.TILE_SIZE)  # x-coord of column in 2D grid

        if self.board[row][column] is None:  # square must initially be blank
            # determine which square the click corresponds to
            square = self.canvas.find_closest(event.x, event.y)[0]
            # fill clicked square with red (user's color)
            self.canvas.itemconfigure(square, fill='#f96167')
            # assign 'user' to the square's place in 2D grid
            self.board[row][column] = 'user'

            # computer's turn
            if not self.display_winner():  # if the game has not yet ended
                int1 = random.randint(0, 2)
                int2 = random.randint(0, 2)

                # random ints must correspond to coordinates of a blank tile
                while self.board[int2][int1] is not None:
                    int1 = random.randint(0, 2)
                    int2 = random.randint(0, 2)

                # determine which square the ints correspond to
                square = self.canvas.find_closest(int1 * self.TILE_SIZE,
                                                  int2 * self.TILE_SIZE)[0]
                # fill chosen square with yellow (computer's color)
                self.canvas.itemconfigure(square, fill='#fce77d')
                # assign 'computer' to the square's place in 2D grid
                self.board[int2][int1] = 'computer'

                self.display_winner()  # check if game has been won

    def check_win(self):
        """
        Check if either user or computer has won the game

        :return: intersection of winners and win_combos set (set)
        """
        # instantiate winner sets
        winners = {('user', 'user', 'user'),
                   ('computer', 'computer', 'computer')}

        # create a set of winning combinations
        # add winning diagonals to the set
        win_combos = {(self.board[0][0], self.board[1][1], self.board[2][2]),
                      (self.board[0][2], self.board[1][1], self.board[2][0])}

        # add winning rows to the set
        for i in range(3):
            win_combos.add((self.board[i][0],
                            self.board[i][1],
                            self.board[i][2]))

        # add winning columns to the set
        for j in range(3):
            win_combos.add((self.board[0][j],
                            self.board[1][j],
                            self.board[2][j]))

        return winners & win_combos

    def display_winner(self):
        """
        Display the winner if someone has won or game ends in a draw

        :return: True if someone has won, False otherwise (boolean)
        """
        self.moves += 1  # increment move counter by 1
        message = ''  # instantiate a blank display message
        winner = self.check_win()  # get winner (if there is one)

        if winner:
            name = winner.pop()[0]

            if name == 'user':
                message = 'You won!'
            else:
                message = 'You lost!'

        else:
            if self.moves == len(self.board)**2:
                message = 'It\'s a tie!'

        if message:  # if message has been changed
            self.outcome_message.config(text=message)  # display new message
            self.canvas.unbind('<Button-1>')  # unbind left clicks on canvas
            return True  # someone has won
        else:
            return False  # game continue


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our Game object
    tic_tac_toe = Game(root)

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
