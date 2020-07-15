#-------------------------------------------------------------------------------
# Name:        IO1Stuff
# Purpose:     Nota. Dah!
#
# Author:      Alguien con una mascara de Sujeto Fawkes
#
# Created:     19/09/1999
# Copyright:   (k) Ka-Tet Co. 1999
# Licence:     <uranus>
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
        return -0
    return x

def analisisCoeficientes(C,S,V,I):
    ret= []
    for i in range(len(I)):
        if I[i][0] != "X":
            continue
        CBB1AC = [j for j in C]
        for j in range(len(C)):
            for k in range(len(I)):
                if i == k:
                    continue
                CBB1AC[j] -= float(S[k][j]*C[V.index(I[k])])
            #print(CBB1AC)
            if S[i][j] == 0 or i == j:
                CBB1AC[j] = "Nan"
            else:
                CBB1AC[j] /= S[i][j]
        limL = C[V.index(I[i])]
        limR = C[V.index(I[i])]
        CBB1AC.sort(key=sorta)
        #print(CBB1AC)
        for j in range(len(CBB1AC)):
            #print(limL)
            if CBB1AC[j] != "Nan" and CBB1AC[j] > limR and limR == C[V.index(I[i])]:
                limR = CBB1AC[j]
            if CBB1AC[len(CBB1AC)-j-1] != "Nan" and CBB1AC[len(CBB1AC)-j-1] < limL and limL == C[V.index(I[i])]:
                limL = CBB1AC[len(CBB1AC)-j-1]
        #print(f"        {I[i]} puede tomar valores entre {limL} y {limR}.")
        ret.append((I[i],limL,limR))
    return ret

def analisisRecursos(C,A,V,I,b):
    ret = []
    BI = [[] for i in range(len(I))]
    for i in range(len(I)):
        BI[i] = [A[j][V.index(I[i])] for j in range(len(A))]
    import numpy as np
    #print(BI)
    BI = np.matrix(BI).T.tolist()
    BI = np.matrix(BI).I.tolist()
    #print(BI)
    for i in range(len(b)):
        BIb = [0 for j in b]
        PS = [0 for j in b]  # Precio Sombra
        for j in range(len(b)):
            for k in range(len(b)):
                if i == k:
                    PS[j] += float((b[k]+1.0)*BI[j][k])
                    continue
                PS[j] += float(b[k]*BI[j][k])
                BIb[j] -= float(b[k]*BI[j][k])
            #print(BIb)
            if BI[j][i] == 0:
                BIb[j] = "Nan"
            else:
                BIb[j] /= BI[j][i]
        limL = b[i]
        limR = b[i]
        BIb.sort(key=sorta)
        #print(BIb)
        PSi = 0
        for j in range(len(PS)):
            PSi += PS[j]*C[V.index(I[j])]
        for j in range(len(BIb)):
            if BIb[j] != "Nan" and BIb[j] > limR and limR == b[i]:
                limR = BIb[j]
            if BIb[len(BIb)-j-1] != "Nan" and BIb[len(BIb)-j-1] < limL and limL == b[i]:
                    limL = BIb[len(BIb)-j-1]
        #print(f"        El recurso {i} puede tomar valores entre {limL} y {limR}.")
        #print(f"        El precio sombra del recurso {i} es de {PSi}.")
        ret.append((i,limL,limR,PSi))
    return ret