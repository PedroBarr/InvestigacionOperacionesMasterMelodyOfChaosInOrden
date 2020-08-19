#-------------------------------------------------------------------------------
# Name:        Modulo de Iteracion Simplex
# Purpose:     Brindar una vista detallada de la solucion a traves de tablas
#              simplex correspondientes al problema
#
# Authors:      Barrera Alfonso, Pedro 20171020057
#              González Mendoza, Sebastián 20172020039
#              Gutiérrez Gómez, Cristian Camilo 20172020046
#
# Created:     19/09/2020
# Copyright:   (k) Ka-Tet Co. 1999
#-------------------------------------------------------------------------------

try: # Importa tkinter, con la excepcion por version de python (ver manual de usuario)
    import Tkinter as tk
    from Tkinter import ttk
except ImportError:
    import tkinter as tk
    from tkinter import ttk

def mkSimplex():
    try:
        import pickle # Importa pickle para poder almacenar archivos del usuario
        state = open("simplex.txt", "wb") # Guarda el problema en la cola de archivos
        pickle.dump(prob, state)
        state.close()
    except: print("No se ha podido guardar") # Imprime un Error en caso de no poder guardar el problema

def gmSimplex():
    try:
        import pickle # Importa pickle para poder almacenar archivos del usuario
        stated = open("simplex.txt", "rb") # Carga el problema almacenado en la cola de archivos
        spx = pickle.load(stated)
        stated.close()
        return spx # Retorna el problema
    except: print("No se ha podido cargar ") # Imprime un Error en caso de no hallar el problema

def gtP():
    mkSimplex() # Almacena el problema actual
    import InterfazPreSimplex # Importa el modulo para el planteamiento de problemas
    InterfazPreSimplex.main(marco) # Ejecuta el modulo de planteamientos, destruyendose a si mismo

def gtS():
    prob.solucionar(1) # Itera el problema 1 vez
    mkSimplex() # Almacena el problema actual
    main(marco) # Actualiza el marco

def gtA():
    if len(prob.iters) > 1:
        prob.iters.pop() # Destruye la ultima iteracion del problema
        if not prob.brk: prob.brk = True # Pasa el estado del problema a inconcluso si ya estaba solucionado
        mkSimplex() # Almacena el problema actual
        main(marco) # Actualiza el marco

def gtDr():
    prob.solucionar() # Soluciona el problema
    mkSimplex() # Almacena el problema actual
    main(marco) # Actualiza el marco

def gtAS():
    prob.solucionar() # Soluciona el problema
    mkSimplex() # Almacena el problema actual
    import InterfazProblema # Importa el modulo para el reporte completo del problema
    InterfazProblema.main() # Ejecuta el modulo de reporte, destruyendose a si mismo

def imprimirTab(frame):
    for l in frame.grid_slaves(): l.destroy() # Destruye los elementos en el marco
    tk.Label(frame, text=f"Tabla de Iteracion {len(prob.iters)-1}",
            bg="#606060",fg="white", borderwidth=2
            ,relief="groove").grid(row=0, column=1, columnspan=len(prob.Z)+3,
                                   sticky="NSWE") # Imprime el numero de iteracion
    tk.Label(frame, text=f"Z",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=1, column=1,sticky="NSWE") # Imprime Z
    for i in range(len(prob.Z)):
        tk.Label(frame, text=f"{prob.iters[-1].Z[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=1, column=i+2,sticky="NSWE") # Imprime los coeficientes de Z actuales
    tk.Label(frame, text=f"Vb",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=2, column=1,sticky="NSWE") # Imprime Vb
    for i in range(len(prob.V)):
        tk.Label(frame, text=f"{prob.V[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=2, column=i+2,sticky="NSWE") # Imprime las etiquetas del problema
    for i in range(len(prob.S)):
        tk.Label(frame, text=f"{prob.iters[-1].I[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=i+3, column=1,sticky="NSWE") # Imprime las etiquetas solucion
        for j in range(len(prob.Z)):
            tk.Label(frame, text=f"{prob.iters[-1].S[i][j]}",bg="#606060",
                     fg="white", borderwidth=2,
                     relief="groove").grid(row=i+3, column=j+2,sticky="NSWE") # Imprime el recurso j de la variable i
        tk.Label(frame, text=f"{prob.iters[-1].R[i]}",bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=i+3, column=len(prob.Z)+2,sticky="NSWE") # Imprime el limite de la variable i
    try:
        if prob.brk:
            prob.iters[-1].iterar() # Calcula las salidas y entradas de la tabla
            s=f"Sale {prob.iters[-1].I[prob.iters[-1].out]} y entra {prob.V[prob.iters[-1].ind]}" # Asigna S si
        else: s="No se puede iterar más el ejercicio" # Asigna S si no
    except: s="No se puede iterar más el ejercicio" # Asigna S si error
    finally:
        tk.Label(frame, text=s,bg="#606060",fg="white", borderwidth=2,
            relief="groove").grid(row=10, column=0,columnspan=len(prob.Z)+3,sticky="NSWE") # Imprime S

def mkItr():
    for l in marco.grid_slaves(): l.destroy() # Destruye los elementos en el marco
    marco.configure(background='#202020') # Estiliza el marco
    marco.title(f'Iteracion {len(prob.iters)-1}') # Rotula el marco
    tk.Label(marco, text="Optimizador de soluciones - Grupo 5",bg="#202020",fg="white").grid(row=0, column=0, columnspan=7) # Imprime

    #parte de Iter
    frItr = tk.Frame(marco,bg="#202020") # Agrega el frame al marco
    frItr.grid(row=1, column=0, columnspan=7)
    imprimirTab(frItr) # Imprime tabla en el frame

    #parte de goingto
    frGt = tk.Frame(marco,bg="#202020") # Agrega el frame al marco
    frGt.grid(row=4, column=0, columnspan=7)
    btnGtP=tk.Button(frGt, text='Plantear Nuevamente', command=gtP).grid(row=0, column=0) # Agrega boton
    if len(prob.iters) > 1:
        btnGtA=tk.Button(frGt, text='Anterior', command=gtA).grid(row=0, column=1) # Agrega boton si
    if prob.brk:
        btnGtS=tk.Button(frGt, text='Siguiente', command=gtS).grid(row=0, column=2) # Agrega boton si
        btnGtD=tk.Button(frGt, text='Solucion directa', command=gtDr).grid(row=0, column=3) # Agrega boton si
    else: btnGtD=tk.Button(frGt, text='Mostrar Analisis', command=gtAS).grid(row=0, column=3) # Agrega boton si no

prob = None # Inicializa el problema
marco = None # Inicializa el marco

def main(orig:None=None):
    global prob, marco
    prob = gmSimplex() # Carga el problema almacenado
    if prob:
        if orig: marco = orig # Inicializa el marco si
        else: marco = tk.Tk() # Inicializa el marco si no
        mkItr() # Itera el problema si
        marco.mainloop() # Ejecuta el marco si
    else:
        import InterfazPreSimplex # Importa el modulo para el planteamiento de problemas si no
        InterfazPreSimplex.main() # Ejecuta el modulo de planteamientos, destruyendose a si mismo si no

if __name__ == '__main__':
    main()
