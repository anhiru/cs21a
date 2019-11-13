# ----------------------------------------------------------------------------
# Name:         game
# Purpose:      implement a generic board game using Tkinter
#
# Author:       Andrew Tran
# Date:         06/15/2019
# ----------------------------------------------------------------------------
"""
Module to implement a generic GUI board game app
"""
import tkinter


class Game(object):
    """
    GUI Game class to support a general-purpose 8x8 board game

    Arguments:
    parent: the root window object (tkinter.Tk)

    Attributes:
    parent: the root window object (tkinter.Tk)
    canvas: the canvas representing the game board (tkinter.Tk)
    """
    # specify a class variable for the tile_size
    tile_size = 50

    def __init__(self, parent):
        parent.title('CS 21A Board Game')

        # save the parent as an instance variable
        # so that it can be accessed by the draw_board method
        self.parent = parent

        # create a START button and associate it with the start method
        # note that we specify self.start and NOT self.start() as the command
        start_button = tkinter.Button(self.parent, text='START',
                                      width=20, command=self.start)

        # register it with a geometry manager -- in this case, grid()
        start_button.grid()

        # create a STOP button and associate it with the stop method
        # note that we specify self.quit and NOT self.quit() as the command
        quit_button = tkinter.Button(self.parent, text='STOP',
                                     width=20, command=self.quit)

        # register it with a geometry manager -- in this case, grid()
        quit_button.grid()

        self.draw_board()

    def draw_board(self):
        """
        Draw a red and black checkered pattern on the game board

        :return: None
        """
        # create a canvas to draw our board
        self.canvas = tkinter.Canvas(self.parent,
                                     width=self.tile_size * 8,
                                     height=self.tile_size * 8)

        # register it with a geometry manager
        self.canvas.grid()

        # draw the tiles on the canvas
        for row in range(8):
            for column in range(8):
                if (row + column) % 2 == 0:
                    color = 'black'
                else:
                    color = 'red'

                self.canvas.create_rectangle(self.tile_size * column,
                                             self.tile_size * row,
                                             self.tile_size * (column + 1),
                                             self.tile_size * (row + 1),
                                             fill=color)

    def start(self):
        """
        Start the game -- print a message to show that the user has pressed
        the START button

        :return: None
        """
        print('Starting the game...')

    def quit(self):
        """
        Quit the game -- print a message to show that the user has pressed
        the QUIT button

        :return: None
        """
        print('Quitting the game...')


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our Game object
    generic_game = Game(root)

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
