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

varX=[]
varS=[]
varP=[]
varB=[]
prob = None

def smSimplex():
        import pickle
        state = open("simplex.txt", "wb")
        pickle.dump(prob, state)
        state.close()

def mkSimplex():
    import Simplex_M_Dual_DosFases as Spx
    import pickle
    global prob
    try: prob = Spx.Simplex([i.get() for i in varX],
                            [[j.get() for j in i] for i in varS],
                            [i.get() for i in varP],
                            [i.get() for i in varB],
                            str(obj.get()[:3]))
    except:
        print("algo a fuido mucho mas mal de lo esperado")
    finally: smSimplex()

def bldZn():
    global varX
    for l in frZ.grid_slaves(): l.destroy()
    tk.Label(frZ, text="Z=",bg="#202020",fg="white").grid(row=0, column=0)
    try:
        varX = [tk.IntVar() for i in range(int(varZn.get()))]
        for i in range(int(varZn.get())):
            tk.Entry(frZ, textvariable = varX[i], width="5").grid(row=0, column=2*i+1)
            tk.Label(frZ, text=f"X{i+1}"+ str("+" if i != int(varZn.get())-1 else ""),bg="#202020",fg="white").grid(row=0, column=2*(i+1))
    except:
        print("Debe ingresar un numero en el campo para Z")
        varZn.set(0)
        bldZn()

def bldSn():
    global varS,varP,varB
    for l in frS.grid_slaves(): l.destroy()
    try: rest = int(varSn.get())
    except:
        print("Debe ingresar un numero en el campo para S.A.")
        varSn.set(0)
        bldSn()
        return
    try: Vs = int(varZn.get())
    except: bldZn(); return
    #try:
    tk.Label(frS, text="SA:",bg="#202020",fg="white").grid(row=int(rest/2), column=0)
    canvas = tk.Canvas(frS, width=5, height=5, bg="#202020")
    canvas.grid(row=0, column=1, rowspan = int(rest if rest!= 0 else 1), sticky="NS")
    varS = [[tk.IntVar() for i in range(Vs)]  for j in range(rest)]
    varB = [tk.IntVar() for i in range(rest)]
    varP = [ttk.Combobox(frS, state="readonly", width="3") for i in range(rest)]
    for i in range(rest):
        for j in range(Vs):
            tk.Entry(frS, textvariable = varS[i][j], width="5").grid(row=i, column=2*(j+1))
            tk.Label(frS, text=f"X{i+1}"+ str("+" if j != Vs-1 else ""),bg="#202020",fg="white").grid(row=i, column=2*j+3)
        varP[i]["values"] = ["<=", "==",">="]
        varP[i].set("<=")
        varP[i].grid(row=i, column=2*Vs+4)
        tk.Entry(frS, textvariable = varB[i], width="5").grid(row=i, column=2*Vs+5)
    #except: print("???")

def gtSt():
    mkSimplex()
    '''try: prob.solucionar(0); smSimplex()
    except:
        print("ha ocurrido un error inesperado al desarrollar el tablero simplex")
        return'''
    import InterfazIteracion
    InterfazIteracion.main(marco)

def gtDr():
    mkSimplex()
    try: prob.solucionar(); smSimplex()
    except:
        print("ha ocurrido un error inesperado al desarrollar el tablero simplex")
        return
    import InterfazIteracion
    InterfazIteracion.main(marco)

def gtAs():
    mkSimplex()
    try: prob.solucionar(); smSimplex()
    except:
        print("ha ocurrido un error inesperado al desarrollar el tablero simplex")
        return
    import InterfazProblema
    InterfazProblema.main()

def mkPln():
    global frZn, varZn, txtZn, btnZn, frZ, frSn, varSn, txtSn, btnSn, frS, frO, obj, frGt, btnGtS, btnGtD, btnGtA
    for l in marco.grid_slaves(): l.destroy()
    marco.configure(background='#202020')
    marco.title('Planteamiento - Simplex')
    tk.Label(marco, text="Optimizador de soluciones - Grupo 5",bg="#202020",fg="white").grid(row=0, column=0, columnspan=7)

    #parte de Z
    frZn = tk.Frame(marco,bg="#202020")
    frZn.grid(row=1, column=0, columnspan=7)
    tk.Label(frZn, text="Describa la funcion a optimizar:",bg="#202020",fg="white").grid(row=0, column=0, columnspan=7)
    tk.Label(frZn, text="Numero de variables:",bg="#202020",fg="white").grid(row=2, column=0)
    varZn=tk.IntVar()
    txtZn=tk.Entry(frZn,textvariable=varZn)
    txtZn.grid(row=2, column=1)
    btnZn=tk.Button(frZn, text='Construir Z', command=bldZn).grid(row=1, column=2, rowspan=2, columnspan=2)
    frZ = tk.Frame(frZn,bg="#202020")
    frZ.grid(row=1, column=4, columnspan=5, rowspan=2)

    #parte de S
    frSn = tk.Frame(marco,bg="#202020")
    frSn.grid(row=2, column=0, columnspan=7)
    tk.Label(frSn, text="Describa las restricciones:",bg="#202020",fg="white").grid(row=0, column=0, columnspan=7)
    tk.Label(frSn, text="Numero de recursos:",bg="#202020",fg="white").grid(row=1, column=0)
    varSn=tk.IntVar()
    txtSn=tk.Entry(frSn,textvariable=varSn)
    txtSn.grid(row=1, column=1)
    btnSn=tk.Button(frSn, text='Construir tablero S.A.', command=bldSn).grid(row=1, column=2)
    frS = tk.Frame(frSn,bg="#202020")
    frS.grid(row=2, column=0, columnspan=7)

    #parte de O
    frO = tk.Frame(marco,bg="#202020")
    frO.grid(row=3, column=0, columnspan=7)
    tk.Label(frO, text="El objetivo es: ",bg="#202020",fg="white").grid(row=0, column=0)
    obj = ttk.Combobox(frO, state="readonly")
    obj["values"] = ["Maximizar", "Minimizar"]
    obj.set("Maximizar")
    obj.grid(row=0, column=1)

    #parte de goingto
    frGt = tk.Frame(marco,bg="#202020")
    frGt.grid(row=4, column=0, columnspan=7)
    btnGtS=tk.Button(frGt, text='Paso a Paso', command=gtSt).grid(row=0, column=1)
    btnGtD=tk.Button(frGt, text='Solucion directa', command=gtDr).grid(row=0, column=2)
    btnGtA=tk.Button(frGt, text='Solo analisis', command=gtAs).grid(row=0, column=3)

marco = None

# componentes
frZn = None
varZn = None
txtZn = None
btnZn = None
frZ = None
frSn = None
varSn = None
txtSn = None
btnSn = None
frS = None
frO = None
obj = None
frGt = None
btnGtS = None
btnGtD = None
btnGtA = None

def main(orig:None=None):
    global marco
    if orig: marco = orig
    else: marco = tk.Tk()
    mkPln()
    marco.mainloop()

if __name__ == '__main__':
    main()
