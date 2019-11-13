# ----------------------------------------------------------------------------
# Name:         gui
# Purpose:      demonstrate a GUI application with Tkinter
#
# Author:       Andrew Tran
# Date:         06/15/2019
# ----------------------------------------------------------------------------
"""
Create a GUI application with Tkinter
"""
# import the Tkinter module
import tkinter


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # customize our GUI application main window
    root.title('CS 21A')

    # instantiate a Label widget with root as the parent widget
    # use the text option to specify the text to display
    header = tkinter.Label(root, text='Let\'s Draw!')

    # invoke the pack method on the widget
    header.pack()

    # change the text
    header.configure(text='All Done!')

    # add a background color
    header.configure(background='red')

    # instantiate a Canvas widget with root as the parent widget
    canvas = tkinter.Canvas(root, background='green')

    # draw a blue rectangle on the canvas
    # create_rectangle returns an object ID that we save in the variable body
    body = canvas.create_rectangle(50, 50, 150, 100, fill='blue')

    # draw two red ovals on the canvas
    # create_oval returns an object ID that we save in the variables wheel#
    wheel1 = canvas.create_oval(50, 100, 75, 125, fill='red')
    wheel2 = canvas.create_oval(125, 100, 75, 125, fill='red')

    # draw a line on the canvas
    # create_line returns an object ID that we save in the variable line
    line = canvas.create_line(50, 50, 150, 200)
    canvas.pack()

    # add a color and a width to the line
    canvas.itemconfigure(line, fill='pink', width=10)

    # change the background color of canvas to yellow
    canvas.configure(background='yellow')

    # create a top frame
    top_frame = tkinter.Frame(root)
    top_frame.pack()

    # and a bottom frame
    bottom_frame = tkinter.Frame(root)
    # side is an optional parameter of the pack method, default=tkinter.TOP
    bottom_frame.pack(side=tkinter.BOTTOM)

    # create a STOP button
    stop_button = tkinter.Button(root, text='STOP')
    stop_button.pack()

    # create a GO button
    go_button = tkinter.Button(root, text='GO')
    go_button.pack()

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
