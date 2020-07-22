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

def mkSimplex():
    try:
        import pickle
        state = open("simplex.txt", "wb")
        pickle.dump(prob, state)
        state.close()
    except: print("No se ha podido guardar")

def gmSimplex():
    try:
        import pickle
        stated = open("simplex.txt", "rb")
        spx = pickle.load(stated)
        stated.close()
        return spx
    except: print("No se ha podido cargar ")

def gtP():
    mkSimplex()
    import InterfazPreSimplex
    InterfazPreSimplex.main(marco)

def gtS():
    prob.solucionar(1)
    mkSimplex()
    main(marco)

def gtA():
    if len(prob.iters) > 1:
        prob.iters.pop()
        if not prob.brk: prob.brk = True
        mkSimplex()
        main(marco)

def gtDr():
    prob.solucionar()
    mkSimplex()
    main(marco)

def gtAS():
    prob.solucionar()
    mkSimplex()
    import InterfazProblema
    InterfazProblema.main()

def imprimirTab(frame):
    for l in frame.grid_slaves(): l.destroy()
    tk.Label(frame, text=f"Tabla de Iteracion {len(prob.iters)-1}",
            bg="#606060",fg="white", borderwidth=2
            ,relief="groove").grid(row=0, column=1, columnspan=len(prob.Z)+3,
                                   sticky="NSWE")
    tk.Label(frame, text=f"Z",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=1, column=1,sticky="NSWE")
    for i in range(len(prob.Z)):
        tk.Label(frame, text=f"{prob.iters[-1].Z[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=1, column=i+2,sticky="NSWE")
    tk.Label(frame, text=f"Vb",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=2, column=1,sticky="NSWE")
    for i in range(len(prob.V)):
        tk.Label(frame, text=f"{prob.V[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=2, column=i+2,sticky="NSWE")
    for i in range(len(prob.S)):
        tk.Label(frame, text=f"{prob.iters[-1].I[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=i+3, column=1,sticky="NSWE")
        for j in range(len(prob.Z)):
            tk.Label(frame, text=f"{prob.iters[-1].S[i][j]}",bg="#606060",
                     fg="white", borderwidth=2,
                     relief="groove").grid(row=i+3, column=j+2,sticky="NSWE")
        tk.Label(frame, text=f"{prob.iters[-1].R[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=i+3, column=len(prob.Z)+2,sticky="NSWE")
    try:
        if prob.brk:
            prob.iters[-1].iterar()
            s=f"Sale {prob.iters[-1].I[prob.iters[-1].out]} y entra {prob.V[prob.iters[-1].ind]}"
        else: s="No se puede iterar más el ejercicio"
    except: s="No se puede iterar más el ejercicio"
    finally:
        tk.Label(frame, text=s,bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=10, column=0,columnspan=len(prob.Z)+3,sticky="NSWE")

def mkItr():
    for l in marco.grid_slaves(): l.destroy()
    marco.configure(background='#202020')
    marco.title(f'Iteracion {len(prob.iters)-1}')
    tk.Label(marco, text="Optimizador de soluciones - Grupo 5",bg="#202020",fg="white").grid(row=0, column=0, columnspan=7)

    #parte de Iter
    frItr = tk.Frame(marco,bg="#202020")
    frItr.grid(row=1, column=0, columnspan=7)
    imprimirTab(frItr)

    #parte de goingto
    frGt = tk.Frame(marco,bg="#202020")
    frGt.grid(row=4, column=0, columnspan=7)
    btnGtP=tk.Button(frGt, text='Plantear Nuevamente', command=gtP).grid(row=0, column=0)
    if len(prob.iters) > 1:
        btnGtA=tk.Button(frGt, text='Anterior', command=gtA).grid(row=0, column=1)
    if prob.brk:
        btnGtS=tk.Button(frGt, text='Siguiente', command=gtS).grid(row=0, column=2)
        btnGtD=tk.Button(frGt, text='Solucion directa', command=gtDr).grid(row=0, column=3)
    else: btnGtD=tk.Button(frGt, text='Mostrar Analisis', command=gtAS).grid(row=0, column=3)

prob = None
marco = None

def main(orig:None=None):
    global prob, marco
    prob = gmSimplex()
    if prob:
        if orig: marco = orig
        else: marco = tk.Tk()
        mkItr()
        marco.mainloop()
    else:
        import InterfazPreSimplex
        InterfazPreSimplex.main()

if __name__ == '__main__':
    main()
