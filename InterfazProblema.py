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

try:
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

def gmSimplex():
    try:
        import pickle
        stated = open("simplex.txt", "rb")
        spx = pickle.load(stated)
        stated.close()
        return spx
    except:
        print("No se ha podido cargar ")

def bldAS():
    for l in frame.grid_slaves(): l.destroy()

    prob=gmSimplex()
    prob.solucionar()
    tk.Label(frame, text="PROBLEMA PLANTEADO:", width=100).pack()
    #print(prob)
    s="Z = "
    for i in [f"{prob.Z[i]}{prob.V[i]}"+str(" + " if i!=len(prob.Z)-1 else " ") for i in range(len(prob.Z))]: s+=i
    tk.Label(frame, text=s).pack()
    tk.Label(frame, text=f"").pack()
    tk.Label(frame, text=f"").pack()
    tk.Label(frame, text="RESTRICCIONES:").pack()
    for j in range(len(prob.S)):
        s=""
        for i in [f"{prob.S[j][i]}{prob.V[i]}"+str(" + " if i!=len(prob.Z)-1 else " ") for i in range(len(prob.Z))]: s+=i
        s+=f"{prob.P[j]} {prob.B[j]}"
        tk.Label(frame, text=s).pack()
        tk.Label(frame, text=f"").pack()
    import AnalisisSensibilidad as ASS
    tk.Label(frame, text=f"").pack()
    tk.Label(frame, text="SOLUCION:").pack()
    tk.Label(frame, text=f"Z = {prob.calcularZ()}").pack()
    for j in range(len(prob.I)):
        tk.Label(frame, text=f"{prob.iters[-1].I[j]} = {prob.iters[-1].R[j]}").pack()
    tk.Label(frame, text=f"").pack()
    tk.Label(frame, text="ANALISIS DE COEFICIENTES:").pack()
    for j in ASS.analisisCoeficientes(prob.Z,prob.iters[-1].S,prob.V,prob.iters[-1].I):
        tk.Label(frame, text=f"{j[0]} puede tomar valores entre {j[1]} y {j[2]}.").pack()
        tk.Label(frame, text=f"").pack()
    tk.Label(frame, text=f"").pack()
    tk.Label(frame, text="ANALISIS DE RECURSOS:").pack()
    for j in ASS.analisisRecursos(prob.Z,prob.S,prob.V,prob.iters[-1].I,prob.B):
        tk.Label(frame, text=f"El recurso {j[0]} puede tomar valores entre {j[1]} y {j[2]}.").pack()
        tk.Label(frame, text=f"El precio sombra del recurso {j[0]} es de {j[3]}.").pack()
        tk.Label(frame, text=f"").pack()



marco = tk.Tk()
marco.title('Solucion a Problema')
marco.geometry("+%d+%d" % (25, 25))
marco.configure(background='#202020')

#definicion
tk.Label(marco, text="Optimizador de soluciones - Grupo 5",bg="#202020",fg="white").pack()
frame = tk.Frame(marco, width=100, height=500)
frame.pack()

bldAS()

def main():
    marco.mainloop()

if __name__ == '__main__':
    main()
