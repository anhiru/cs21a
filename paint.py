# ----------------------------------------------------------------------------
# Name:         paint
# Purpose:      a simple coloring application
#
# Author:       Andrew Tran
# Date:         06/15/2019
# ----------------------------------------------------------------------------
"""
Module to implement a simple coloring application using Tkinter
"""
import tkinter


class PaintApp(object):
    """
    GUI PaintApp class for a simple coloring application

    Arguments:
    parent: the root window object (tkinter.Tk)

    Attributes:
    canvas: the widget defining the area to be painted (tkinter.Canvas)
    color: the paint color selected - red, green or blue (string)
    """

    # define a class variable for the default color to be used
    default_color = 'red'

    def __init__(self, parent):
        parent.title("CS 21A - Let's Paint!")

        # create a frame to group all the color buttons
        # this makes it easier to display them all in one row
        color_frame = tkinter.Frame(parent)

        # register it with a geometry manager
        color_frame.grid()

        # create a GREEN button and associate it with the green method
        # we save the button widgets in local variables since no other
        # method needs to access them
        green_button = tkinter.Button(color_frame, text='GREEN',
                                      width=10, command=self.green)

        # register it with a geometry manager
        green_button.grid(column=0, row=0)

        # create a GREEN button and associate it with the red method
        red_button = tkinter.Button(color_frame, text='RED',
                                    width=10, command=self.red)

        # register it with a geometry manager
        red_button.grid(column=1, row=0)

        # create a BLUE button and associate it with the blue method
        blue_button = tkinter.Button(color_frame, text='BLUE',
                                     width=10, command=self.blue)

        # register it with a geometry manager
        blue_button.grid(column=2, row=0)

        # instantiate our Canvas widget with the root as parent
        # since we need to access the canvas widget from the other methods
        # (play and erase), we save it in the object as an instance variable
        self.canvas = tkinter.Canvas(parent, width=300, height=300)

        # draw a rectangle on the canvas for the background
        self.canvas.create_rectangle(0, 0, 300, 300)

        # draw some shapes
        self.canvas.create_rectangle(50, 50, 150, 100)
        self.canvas.create_oval(50, 100, 75, 125)
        self.canvas.create_oval(125, 100, 150, 125)

        # a house
        self.canvas.create_rectangle(175, 150, 275, 250)

        # the roof is a triangle (polygon with 3 sides)
        self.canvas.create_polygon(165, 150, 225, 100, 285, 150,
                                   outline='black')

        # a flower
        self.canvas.create_oval(50, 200, 75, 225)
        self.canvas.create_oval(50, 175, 75, 200)
        self.canvas.create_oval(50, 225, 75, 250)
        self.canvas.create_oval(25, 187, 50, 212)
        self.canvas.create_oval(25, 212, 50, 237)
        self.canvas.create_oval(75, 187, 100, 212)
        self.canvas.create_oval(75, 212, 100, 237)

        # register our canvas with a geometry manager
        self.canvas.grid()

        # when the user clicks on the canvas, we invoke self.paint
        self.canvas.bind("<Button-1>", self.paint)

        # create an ERASER button and associate it with the erase method
        erase_button = tkinter.Button(parent, text='ERASER',
                                      width=30, command=self.erase)

        # register it with a geometry manager
        erase_button.grid()

        # set the paint color to the default color
        self.color = self.default_color

        # fill all the shapes with a white color
        self.erase()

    def erase(self):
        """
        This method is invoked when the ERASE button is clicked.
        It fills all the shapes on the canvas with a white color.
        """
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')

    def green(self):
        """
        This method is invoked when the GREEN button is clicked.
        It sets the paint color to green.
        """
        self.color = "green"

    def red(self):
        """
        This method is invoked when the RED button is clicked.
        It sets the paint color to red.
        """
        self.color = "red"

    def blue(self):
        """
        This method is invoked when the BLUE button is clicked.
        It sets the paint color to blue.
        """
        self.color = "blue"

    def paint(self, event):
        """
        This method is invoked when the user clicks on the canvas.
        It fills the enclosing shape with the current paint color.
        """
        shape = self.canvas.find_closest(event.x, event.y)
        self.canvas.itemconfigure(shape, fill=self.color)


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our painting app object
    painting = PaintApp(root)

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
