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

class Matriz:
    def __init__(self, master, rad, fram):
        global frame, InVal
        frame = fram
        self.clear()
        self.n=rad
        self.lim=19
        self.var_list = {}
        self.RAND()
        frame.grid(row=2, column=0, columnspan=2, rowspan=2)

    def RAND(self):
        self.clear()
        for i in range(self.n):
            for j in range(i, self.n):
                InVal=tk.IntVar()
                val=-1
                if random.randint(0,self.lim)>((self.lim*5.0/8.0)):
                    val=random.randint(3,self.lim)
                self.GetInt(frame, i, j, InVal, val)
                self.GetInt(frame, j, i, InVal, val)
                #print (InVal.get())
                self.var_list[str(i)+","+str(j)] = InVal # stick it into a dict with L as key
                self.var_list[str(j)+","+str(i)] = InVal # stick it into a dict with L as key
        for j in range(self.n):
            InVal=tk.IntVar()
            val=0
            self.GetInt(frame, j, j, InVal, val)
            #print (InVal.get())
            self.var_list[str(j)+","+str(j)] = InVal # stick it into a dict with L as key
            #self.var_list[str(i)+","+str(i)] = InVal # stick it into a dict with L as key

    def GetInt(self, frame, Line, Col, TextVal, InitialVal):
        TextVal.set(str(InitialVal))
        tk.Entry(frame, textvariable=TextVal, width="10").grid(row=Line, column=Col)

    def RUN(self):
        global arbol
        for i in range(self.n):
            for j in range(self.n):
                arbol[i][j]=self.var_list[str(i)+","+str(j)].get() # Now you've got something to reference

    def clear(self):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()

def main():
    pass

if __name__ == '__main__':
    main()
