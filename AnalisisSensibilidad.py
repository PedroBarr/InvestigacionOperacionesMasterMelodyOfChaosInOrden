#-------------------------------------------------------------------------------
# Name:        Modulo de Operaciones para el Analisis de Sensibilidad
# Purpose:     Brindar un paquete con metodos estandarizados, optimos y
#              eficientes para realizar el analisis de la sensibilidad
#              de un problema
#
# Authors:      Barrera Alfonso, Pedro 20171020057
#              González Mendoza, Sebastián 20172020039
#              Gutiérrez Gómez, Cristian Camilo 20172020046
#
# Created:     19/09/2020
# Copyright:   (k) Ka-Tet Co. 1999
#-------------------------------------------------------------------------------

def sorta(x: int) -> int:
    '''
        Ordena una lista ignorando los valores "Nan"
        Parametros:
            x (int, str): valor en la lista
        Return:
            indice de ordenamiento
    '''
    if x == "Nan":
        return -0 # Si es una cadena (str) "Nan" retorna -0 para ordenamiento
    return x

def analisisCoeficientes(C:list,S:list,V:list,I:list):
    '''
        Genera los rangos de utilidad para cada variable en el vector V
        Parametros:
            C (list(int)): lista con los coeficientes de cada variable
                           en el problema base
            S: (list(list(int))): lista con los coeficientes en las
                           restricciones solucion
            V (list(str)): lista con las etiquetas para cada variable
            I (list(str)): lista con las etiquetas para las variables
                           solucion
        Return:
            Lista con tuplas de tres elementos, de la forma:
                (X, limL, limR)
            donde X es la etiqueta de la variable, limL es el limite
            inferior en el rango que puede tomar X y limR es el limite
            superior en el rango que puede tomar X
    '''
    ret= [] # Se crea la lista para los retornos
    for i in range(len(I)):
        if I[i][0] != "X":
            continue # Si la variable actual no es una variable base del problema pasa a la siguiente iteracion (sin hacer los calculos)
        CBB1AC = [j for j in C] # Se crea una lista con los coeficientes de la funcion objetivo
        for j in range(len(C)):
            for k in range(len(I)):
                if i == k:
                    continue # No opera si es la variable que se esta analizando
                CBB1AC[j] -= float(S[k][j]*C[V.index(I[k])]) # Le resta a cada coeficiente el valor original de la funcion objetivo multiplicado por el valor AB(sub(kj))
            #print(CBB1AC)
            if S[i][j] == 0 or i == j:
                CBB1AC[j] = "Nan" # Elimina todos los casos en que no arroja un valor para plantear una inecuacion
            else:
                CBB1AC[j] /= S[i][j] # Reduce el valor para plantear la inecuacion
        limL = C[V.index(I[i])] # Establece como limite por debajo el valor del coeficiente original
        limR = C[V.index(I[i])] # Establece como limite por encima el valor del coeficiente original
        CBB1AC.sort(key=sorta) # Ordena los valores de inecuacion
        #print(CBB1AC)
        for j in range(len(CBB1AC)):
            #print(limL)
            if CBB1AC[j] != "Nan" and CBB1AC[j] > limR and limR == C[V.index(I[i])]:
                limR = CBB1AC[j] # Si halla un valor mayor al limite actual, lo establece como limite por encima
            if CBB1AC[len(CBB1AC)-j-1] != "Nan" and CBB1AC[len(CBB1AC)-j-1] < limL and limL == C[V.index(I[i])]:
                limL = CBB1AC[len(CBB1AC)-j-1] # Si halla un valor menor al limite actual, lo establece como limite por debajo
        #print(f"        {I[i]} puede tomar valores entre {limL} y {limR}.")
        ret.append((I[i],limL,limR)) # Agrega la variable y sus limites a la solucion
    return ret # Devuelve una lista con la solucion para cada variable calculada

def analisisRecursos(C:list,A:list,V:list,I:list,b:list):
    '''
        Genera los rangos de utilidad para cada variable en el vector V
        Parametros:
            C (list(int)): lista con los coeficientes de cada variable
                           en el problema base
            A: (list(list(int))): lista con los coeficientes en las
                           restricciones base
            V (list(str)): lista con las etiquetas para cada variable
            I (list(str)): lista con las etiquetas para las variables
                           solucion
            b (list(int)): lista con los limites en las restricciones
                           base para cada recurso
        Return:
            Lista con tuplas de cuatro elementos, de la forma:
                (R, limL, limR, PS)
            donde R es el numero del recurso, limL es el limite
            inferior en el rango que puede tomar R, limR es el limite
            superior en el rango que puede tomar R y PS es valor de Z
            si R aumenta una unidad
    '''
    ret = [] # Se crea la lista para los retornos
    BI = [[] for i in range(len(I))] # Se crea una matriz para contener las operaciones
    for i in range(len(I)):
        BI[i] = [A[j][V.index(I[i])] for j in range(len(A))] # Se agrega un valor a cada espacio en la matriz, cada valor proviene de las restricciones del problema
    import numpy as np # Se importa numpy (ver manual de usuario)
    #print(BI)
    BI = np.matrix(BI).T.tolist() # Se reemplaza la matriz por su transpuesta
    #print(BI)
    BI = np.matrix(BI).I.tolist() # Se reemplaza la matriz por su inversa
    #print(BI)
    #print(b)
    for i in range(len(b)):
        BIb = [0 for j in b] # Se crea una lista de ceros por cada restriccion
        PS = [0 for j in b]  # Se crea una lista de ceros por cada restriccion donde se almacenaran los precios sombra
        for j in range(len(b)):
            for k in range(len(b)):
                if i == k:
                    PS[j] += float((b[k]+1.0)*BI[j][k]) # Asigna un valor base al precio sombra para la variable que se esta analizando, aumentando uno al recurso
                    continue # No opera los demas calculos si es la variable que se esta analizando
                PS[j] += float(b[k]*BI[j][k]) # Asigna un valor base al precio sombra
                BIb[j] -= float(b[k]*BI[j][k]) # Asigna un valor base para el valor de la inecuacion
            #print(BIb)
            if BI[j][i] == 0:
                BIb[j] = "Nan" # Elimina todos los casos en que no arroja un valor para plantear una inecuacion
            else:
                BIb[j] /= BI[j][i] # Reduce el valor para plantear la inecuacion
        limL = b[i] # Establece como limite por debajo el valor del valor original del recurso
        limR = b[i] # Establece como limite por encima el valor del valor original del recurso
        BIb.sort(key=sorta) # Ordena los valores de inecuacion
        #print(BIb)
        PSi = 0 # Establece el precio sombra en cero
        for j in range(len(PS)):
            PSi += PS[j]*C[V.index(I[j])] # Suma los precios por recurso para establecer el precio sombra
        for j in range(len(BIb)):
            if BIb[j] != "Nan" and BIb[j] > limR and limR == b[i]:
                limR = BIb[j] # Si halla un valor mayor al limite actual, lo establece como limite por encima
            if BIb[len(BIb)-j-1] != "Nan" and BIb[len(BIb)-j-1] < limL and limL == b[i]:
                limL = BIb[len(BIb)-j-1] # Si halla un valor menor al limite actual, lo establece como limite por encima
        #print(f"        El recurso {i} puede tomar valores entre {limL} y {limR}.")
        #print(f"        El precio sombra del recurso {i} es de {PSi}.")
        ret.append((i,limL,limR,PSi)) # Agrega la variable, sus limites y su precio sombra a la solucion
    return ret # Devuelve una lista con la solucion para cada variable calculada
