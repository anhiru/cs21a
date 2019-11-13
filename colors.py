# ----------------------------------------------------------------------------
# Name:         colors
# Purpose:      example GUI application using Tkinter
#
# Author:       Andrew Tran
# Date:         06/15/2019
# ----------------------------------------------------------------------------
"""
Table of colors using Tkinter
"""
import tkinter


# instantiate color dictionary
COLORS = {'red': 'rouge', 'blue': 'bleu', 'green': 'vert',
          'yellow': 'jaune', 'black': 'noir', 'white': 'blanc'}


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # customize our GUI application main window
    root.title('Colors')

    # add a label
    table_label = tkinter.Label(root, text='Color Palette')

    # register label with a geometry manager -- in this case, grid()
    table_label.grid()

    # instantiate a frame for our table
    table = tkinter.Frame(root)

    # register table with a geometry manager
    table.grid()

    row_count = 0
    # loop through the colors in our dictionary
    for color in COLORS:
        # instantiate a label for the English name
        color_english = tkinter.Label(table, text=color)
        # instantiate a label for the French name
        color_french = tkinter.Label(table, text=COLORS[color])
        # instantiate a label to show the color swatch
        color_swatch = tkinter.Label(table, background=color, width=12)

        # each label goes in a different column -- same row
        color_english.grid(row=row_count, column=0)
        color_french.grid(row=row_count, column=1)
        color_swatch.grid(row=row_count, column=2)

        # increment row count before moving onto next color
        row_count += 1

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
