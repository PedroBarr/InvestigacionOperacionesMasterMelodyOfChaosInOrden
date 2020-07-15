#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LAO BARRERA
#
# Created:     07/06/2020
# Copyright:   (c) LAO BARRERA 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

try: import Tkinter as tk
except ImportError: import tkinter as tk

class Interfaz(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        conten = tk.Frame(self)

        conten.pack(side="top", fill="both", expand = True)

        conten.grid_rowconfigure(0, weight=1)
        conten.grid_columnconfigure(0, weight=1)

        self.frames = {}

        '''for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)'''

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def main():
    marco = Interfaz()
    marco.mainloop()
    pass

if __name__ == '__main__':
    main()
