# ----------------------------------------------------------------------------
# Name:         tictac
# Purpose:      implement a game of Tic Tac Toe
#
# Author:       Andrew Tran
# Date:         06/17/2019
# ----------------------------------------------------------------------------
"""
Module to implement a GUI for a game of Tic Tac Toe

The user always plays first against the computer.
The user is given the option to restart the game at any point
during a game or after a win, loss, or tie.
Whoever succeeds in placing three marks in a horizontal, vertical,
or diagonal line wins the game.
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
    win_scenarios: the list of 8 total possible winning combinations (list)
    """

    TILE_SIZE = 100  # constant length/width of each tile

    def __init__(self, parent):
        self.user_squares = set()
        self.computer_squares = set()
        self.unused_squares = set()

        parent.title('Tic Tac Toe')

        # create a RESTART button and associate it with the restart method
        restart_button = tkinter.Button(parent, text='RESTART',
                                        width=10, command=self.restart)
        # register it with the grid() geometry manager
        restart_button.grid()

        # create a canvas to draw our board
        self.canvas = tkinter.Canvas(parent,
                                     width=self.TILE_SIZE * 3,
                                     height=self.TILE_SIZE * 3)
        # register it with the grid() geometry manager
        self.canvas.grid()

        # draw the tiles on the canvas
        for row in range(3):
            for column in range(3):
                new_square = self.canvas.create_rectangle(
                    self.TILE_SIZE * column,
                    self.TILE_SIZE * row,
                    self.TILE_SIZE * (column + 1),
                    self.TILE_SIZE * (row + 1),
                    fill='#ffffff')
                self.unused_squares.add(new_square)

        # bind left clicks on the canvas to the play method
        self.canvas.bind('<Button-1>', self.play)

        # create a label for the win/lose/tie message
        self.outcome_message = tkinter.Label(parent, text='')
        # register it with the grid() geometry manager
        self.outcome_message.grid()

        # call static method once to obtain winning combinations
        self.win_scenarios = self.get_win_scenarios()

    def restart(self):
        """
        Invoked when the user clicks on the restart button, restarts the game

        :return: None
        """
        # clear player sets
        self.unused_squares = {i for i in range(1, 10)}
        self.user_squares.clear()
        self.computer_squares.clear()

        # revert all squares to white
        for square in self.canvas.find_all():
            self.canvas.itemconfigure(square, fill='#ffffff')

        # rebind left click to self.play
        self.canvas.bind('<Button-1>', self.play)

        # clear outcome message
        self.outcome_message.config(text='')

    def play(self, event):
        """
        Invoked when the user clicks on a square, dictates flow of the game

        :param event: event object giving access to click coordinates (Event)
        :return: None
        """
        # user's turn
        row = (event.y // self.TILE_SIZE)  # row associated with y-coord
        column = (event.x // self.TILE_SIZE)  # column associated with x-coord
        selected_square = row * 3 + column + 1  # convert to square ID (1-9)

        if selected_square in self.unused_squares:  # square must be blank
            # determine which square the click corresponds to
            square = self.canvas.find_closest(event.x, event.y)[0]
            # fill clicked square with red (user's color)
            self.canvas.itemconfigure(square, fill='#f96167')
            # add clicked square to user_squares
            self.user_squares.add(selected_square)
            # remove clicked square from unused_squares
            self.unused_squares.remove(selected_square)

            # computer's turn
            if not self.check_win():  # if the user has not already won
                row, column = self.computer_move()  # get tuple of coordinates

                # determine which square the coordinates correspond to
                square = self.canvas.find_closest(row * self.TILE_SIZE,
                                                  column * self.TILE_SIZE)[0]
                # fill chosen square with yellow (computer's color)
                self.canvas.itemconfigure(square, fill='#fce77d')

                self.check_loss()  # check if the computer has won the game

    def check_win(self):
        """
        Check if user has won the game

        :return: True if user has won the game, False otherwise (boolean)
        """
        for win in self.win_scenarios:
            if self.user_squares >= win:  # user_squares is a superset of win
                self.outcome_message.config(text='You won!')
                self.canvas.unbind('<Button-1>')
                return True
        else:
            if not self.unused_squares:  # no blank tiles remaining
                self.outcome_message.config(text='It\'s a tie!')
                self.canvas.unbind('<Button-1>')
                return True
            else:
                return False

    def check_loss(self):
        """
        Check if user has lost the game

        :return: None
        """
        for win in self.win_scenarios:
            if self.computer_squares >= win:  # computer_squares is a superset
                self.outcome_message.config(text='You lost!')
                self.canvas.unbind('<Button-1>')

    def computer_move(self):
        """
        Algorithm for determining the computer's move

        :return: coordinates representing square's space in 2D grid (tuple)
        """
        # loop through remaining blank tiles
        for blank_square in self.unused_squares:
            # if computer has 2 squares in a line and the third square is open
            # the computer will mark it to win
            self.computer_squares.add(blank_square)
            for win in self.win_scenarios:
                if self.computer_squares >= win:
                    # convert blank_square ID to canvas coordinates
                    x_coordinate = (blank_square - 1) // 3
                    y_coordinate = (blank_square + 2) % 3

                    self.unused_squares.remove(blank_square)

                    return y_coordinate, x_coordinate
            else:
                self.computer_squares.remove(blank_square)

        # loop through remaining blank tiles
        for blank_square in self.unused_squares:
            # if the user has 2 squares in a line and the third square is open
            # the computer will block it
            self.user_squares.add(blank_square)
            for win in self.win_scenarios:
                if self.user_squares >= win:
                    # convert blank_square ID to canvas coordinates
                    x_coordinate = (blank_square - 1) // 3
                    y_coordinate = (blank_square + 2) % 3

                    self.user_squares.remove(blank_square)
                    self.computer_squares.add(blank_square)
                    self.unused_squares.remove(blank_square)

                    return y_coordinate, x_coordinate
            else:
                self.user_squares.remove(blank_square)

        if 5 not in self.unused_squares:  # if the middle square is not open
            # choose random square ID from 1-9
            random_int = random.randint(1, 9)
            while random_int not in self.unused_squares:
                random_int = random.randint(1, 9)
            self.computer_squares.add(random_int)
            self.unused_squares.remove(random_int)

            # convert random available square ID to canvas coordinates
            x_coordinate = (random_int - 1) // 3
            y_coordinate = (random_int + 2) % 3

            return y_coordinate, x_coordinate
        else:  # the middle square is open, so prioritize over random squares
            self.computer_squares.add(5)
            self.unused_squares.remove(5)

            return 1, 1  # middle coordinates

    @staticmethod
    def get_win_scenarios():
        """
        Compute all possible winning scenarios for Tic Tac Toe on a 3x3 grid

        :return: list of 8 total possible winning combinations as sets (list)
        """
        # initialize list of winning scenarios
        win_scenarios = [{1, 5, 9}, {3, 5, 7}]  # add diagonals

        # add rows
        for i in range(1, 4):
            win_scenarios.append({i * 3, i * 3 - 1, i * 3 - 2})

        # add columns
        for j in range(1, 4):
            win_scenarios.append({j, j + 3, j + 6})

        return win_scenarios


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our Game object
    tic_tac_toe = Game(root)

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
