#-------------------------------------------------------------------------------
# Name:        Modulo Final Solucion Completa y Reporte
# Purpose:     Generar un reporte general que esclarezca la solucion hallada
#              en lenguaje natural-matematico
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

def gmSimplex():
    try:
        import pickle # Importa pickle para poder almacenar archivos del usuario
        stated = open("simplex.txt", "rb") # Carga el problema almacenado en la cola de archivos
        spx = pickle.load(stated)
        stated.close()
        return spx # Retorna el problema
    except:
        print("No se ha podido cargar ") # Imprime un Error en caso de no hallar el problema

def bldAS():
    for l in frame.grid_slaves(): l.destroy() # Reinicia el marco actual

    prob=gmSimplex() # Carga el problema almacenado
    prob.solucionar() # Genera la solucion del problema
    tk.Label(frame, text="PROBLEMA PLANTEADO:", width=100).pack() # Imprime
    #print(prob)
    s="Z = " # Inicializa la funcion objetivo
    for i in [f"{prob.Z[i]}{prob.V[i]}"+str(" + " if i!=len(prob.Z)-1 else " ") for i in range(len(prob.Z))]: s+=i # Agrega los terminos a la funcion objetivo
    tk.Label(frame, text=s).pack() # Imprime la funcion objetivo
    tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text="RESTRICCIONES:").pack() # Imprime
    for j in range(len(prob.S)):
        s="" # Inicializa la restriccion j
        for i in [f"{prob.S[j][i]}{prob.V[i]}"+str(" + " if i!=len(prob.Z)-1 else " ") for i in range(len(prob.Z))]: s+=i # Agrega los terminos a la restriccion j
        s+=f"{prob.P[j]} {prob.B[j]}" # Agrega los terminos de las holguras a la restriccion j
        tk.Label(frame, text=s).pack() # Imprime la restriccion j
        tk.Label(frame, text=f"").pack() # Imprime
    import AnalisisSensibilidad as ASS # Importa el modulo propio para el Analisis de Sensibilidad
    tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text="SOLUCION:").pack() # Imprime
    tk.Label(frame, text=f"Z = {prob.calcularZ()}").pack() # Imprime el valor de utilidad calculado
    for j in range(len(prob.I)):
        tk.Label(frame, text=f"{prob.iters[-1].I[j]} = {prob.iters[-1].R[j]}").pack() # Imprime los valores de las variables solucion
    tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text="ANALISIS DE COEFICIENTES:").pack() # Imprime
    for j in ASS.analisisCoeficientes(prob.Z,prob.iters[-1].S,prob.V,prob.iters[-1].I):
        tk.Label(frame, text=f"{j[0]} puede tomar valores entre {j[1]} y {j[2]}.").pack() # Imprime el analisis de coeficientes para la variable j
        tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text=f"").pack() # Imprime
    tk.Label(frame, text="ANALISIS DE RECURSOS:").pack() # Imprime
    for j in ASS.analisisRecursos(prob.Z,prob.S,prob.V,prob.iters[-1].I,prob.B):
        tk.Label(frame, text=f"El recurso {j[0]} puede tomar valores entre {j[1]} y {j[2]}.").pack() # Imprime el analisis de recursos para la variable j
        tk.Label(frame, text=f"El precio sombra del recurso {j[0]} es de {j[3]}.").pack() # Imprimeel precio sombra para la variable j
        tk.Label(frame, text=f"").pack() # Imprime



marco = tk.Tk() # Inicializa el marco
marco.title('Solucion a Problema') # Rotula el marco
marco.geometry("+%d+%d" % (25, 25)) # Limita el marco
marco.configure(background='#202020') # Estiliza el marco

#definicion
tk.Label(marco, text="Optimizador de soluciones - Grupo 5",bg="#202020",fg="white").pack() # Imprime
frame = tk.Frame(marco, width=100, height=500) # Agrega el frame al marco
frame.pack() # Agrega el frame al marco

bldAS()

def main():
    marco.mainloop() # Ejecuta el marco

if __name__ == '__main__':
    main()
