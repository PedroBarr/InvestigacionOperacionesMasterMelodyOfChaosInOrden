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

def imprimirT(Z: list, V: list, S: list, B: list, It: int,  I: list) -> None:
    '''
        Imprime una tabla en consola
        Parametros:
            Z (list): coeficientes  de la funcion a optimizar
            V (list): etiquetas de las variables
            S (list): coeficientes en las restricciones
            B (list): inequacion en las restricciones
            It (str): numero de iteracion
            I (list): etiquetas de las variables resultados
        Return:
            Aun no D:<
    '''
    esp = 8 #define numero de espaciado (ED)
    print(f"Tabla de Iteracion {It}")
    print("Z", end=" "*esp)
    for i in Z:
        print(str(i)[:esp-2], end=" "*(esp+1-len(str(i)[:esp-2])))
    print()
    print("Vb", end=" "*(esp-1))
    for i in V:
        print(str(i)[:esp-2], end=" "*(esp+1-len(str(i)[:esp-2])))
    for i in range(len(S)):
        print()
        print(str(I[i])[:esp-2], end=" "*(esp+1-len(str(I[i])[:esp-2])))
        for j in S[i]:
            print(str(j)[:esp-2], end=" "*(esp+1-len(str(j)[:esp-2])))
        print(B[i], end="")
    print()

class Iteracion:
    def __init__(self, Z: list, S: list, R: list, I: list):
        self.Z = Z
        self.S = S
        self.R = R
        self.I = [i for i in I]
        self.out = None
        self.ind = None

    def __str__(self):
        imprimirT(self.Z,["X" for i in self.Z],self.S,self.R,None,self.I)
        return ""

    def calcularZ(self,ZI:list):
        pass

    def iterar(self, O:str = "MAX"):
        Z = [i for i in self.Z]
        S = [[j for j in i] for i in self.S]
        R = [i for i in self.R]
        comp = 0
        for i in Z:
            if abs(i) > abs(comp):
                if O.upper() == "MAX" and i > 0:
                    comp = i
                elif O.upper() == "MIN" and i < 0:
                    comp = i
        #print("Z Mayor:", comp)
        self.ind = Z.index(comp)
        #print("Z Mayor:", comp)
        #print("In-Columna:", ind)
        #print(f"Entra {V[ind]}", end=" y ")
        comp = 999999999
        for i in range(len(R)):
            if S[i][self.ind] > 0 and abs(R[i]/S[i][self.ind]) < abs(comp):
                comp = R[i]/S[i][self.ind]
                self.out = i
        #print("R Menor:", comp)
        #print("Out-Fila:", out)
        #print(f"sale {I[out]}")
        R[self.out] = R[self.out]/S[self.out][self.ind]
        S[self.out] = [i/S[self.out][self.ind] for i in S[self.out]]
        for i in range(len(S)):
            if i != self.out:
                R[i] = R[i]-S[i][self.ind]*R[self.out]
                S[i] = [S[i][j]-S[i][self.ind]*S[self.out][j] for j in range(len(S[i]))]
        Z = [Z[j]-Z[self.ind]*S[self.out][j] for j in range(len(Z))]
        #I[out] = str(V[ind])
        #print()
        return (Z,S,R)

class Simplex:
    def __init__(self, Z: list, S: list, P: list, B: list, O: str):
        if len(S) != len(P) or len(S)!=len(B):
            print("Objeto simplex creado de manera incorrecta")
        self.V = [f"X{i+1}" for i in range(len(Z))]
        self.I = [f"A{i+1}" if P[i] == ">=" or P[i] == "==" or P[i] == "=" else f"S{i+1}" if P[i] == "<=" else None for i in range(len(P))]
        self.P = P
        self.Z = [float(i) for i in Z] + [0.0 for i in P if i == "<=" or i == "==" or i == "=" or
                        i  == ">="] + [0.0 for i in P if i == ">="] # crea la
        self.S = [[float(j) for j in S[i]] for i in range(len(S))]
        for i in range(len(P)):
            if P[i] == "<=":
                for j in range(len(self.S)):
                    self.S[j].append(0.0)
                    if j == i: self.S[j][-1] = 1.0
                self.V.append(f"S{i+1}")
            elif P[i] == "==" or P[i] == "=":
                for j in range(len(self.S)):
                    self.S[j].append(0.0)
                    if j == i: self.S[j][-1] = 1.0
                self.V.append(f"A{i+1}")
            elif P[i] == ">=":
                for j in range(len(self.S)):
                    self.S[j].append(0.0)
                    if j == i: self.S[j][-1] = -1.0
                    self.S[j].append(0)
                    if j == i: self.S[j][-1] = 1.0
                self.V.append(f"S{i+1}")
                self.V.append(f"A{i+1}")
        self.B = [float(i) for i in B]
        self.O = O
        self.iters = []
        self.iters.append(Iteracion(self.Z,self.S,self.B,self.I))
        self.fZ = self.calcularZ()
        self.brk = True
        #print(f"Z {len(Z)} S {len(S)} P {len(P)} B {len(B)}")
        #imprimirT(Z,V,S,B,nI,I)

    def __str__(self, it:int=None):
        if type(it) == int:
            try: imprimirT(self.iters[it].Z,self.V,self.iters[it].S,self.iters[it].R,it,self.iters[it].I)
            except: return f"Index {it} inexistente"
            return ""
        for i in self.iters:
            imprimirT(i.Z,self.V,i.S,i.R,self.iters.index(i),i.I)
            print()
            try:print(f"Entra {self.V[i.ind]} y sale {self.iters[-1].I[i.out]}")
            except: continue

        if len(self.iters) > 1:
            print("Solucion:")
            print(f"    Z: {self.calcularZ()}")
            for i in range(len(self.I)):
                print(f"    {self.I[i]}: {self.iters[-1].R[i]}")
        return ""

    def calcularZ(self):
        h = 0
        #print([self.iters[-1].R[i] for i in range(len(self.I))])
        #print([self.Z[self.V.index(self.iters[-1].I[i])] for i in range(len(self.I))])
        for i in [self.iters[-1].R[i]*self.Z[self.V.index(self.iters[-1].I[i])] for i in range(len(self.I))]: h += i
        return h

    def solucionar(self, n:int=None):
        while self.brk:
            T = self.iters[-1].iterar(self.O)
            self.I[self.iters[-1].out] = str(self.V[self.iters[-1].ind])
            #Z = T[0]
            #S = T[1]
            #B = T[2]
            brk = True
            for i in T[0]:
                if self.O.upper() == "MIN":
                    if i < 0:
                        brk = False
                        break
                if self.O.upper() == "MAX":
                    if i > 0:
                        brk = False
                        break
            self.iters.append(Iteracion(T[0],T[1],T[2],self.I))
            if n: n-=1
            #imprimirT(Z,V,S,B,nI,I)
            if (brk or len(self.iters) - 1 >= len(self.Z) or
                (type(n) == int and n == 0)):
                self.brk = bool(not brk)
                break
        #print()
        #print("Solucion:")
        #for i in range(len(I)):
            #print(f"    {I[i]}: {B[i]}")