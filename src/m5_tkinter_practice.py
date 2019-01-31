"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Brendan Boewe.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    root = tkinter.Tk()

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    go_forward_button = ttk.Button(frame1, text='Forward')
    go_forward_button.grid()

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    go_forward_button['command'] = (lambda: print('Hello'))


    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    hello_goodbye_entry_box = ttk.Entry(frame1)
    hello_goodbye_entry_box.grid()

    hello_goodbye_button = ttk.Button(frame1, text='Hello/Goodbye')
    hello_goodbye_button.grid()

    hello_goodbye_button['command'] = (lambda: hello_goodbye(hello_goodbye_entry_box.get()))



    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    entry_box2 = ttk.Entry(frame1)
    entry_box2.grid()

    entry_box2_button = ttk.Button(frame1, text='Entry Box 2')
    entry_box2_button.grid()

    entry_box2_button['command'] = (lambda: entry_box2_function(entry_box2.get(), hello_goodbye_entry_box.get()))


    # -------------------------------------------------------------------------
    # DONE 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------

    root.mainloop()

def hello_goodbye(contents):
    if contents == 'ok':
        print('Hello')
    else:
        print('Goodbye')

def entry_box2_function(entry2_contents, hello_goodbye_contents):
    x = int(entry2_contents)
    for _ in range(x):
        print(hello_goodbye_contents)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
