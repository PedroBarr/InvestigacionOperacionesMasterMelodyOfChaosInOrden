#-------------------------------------------------------------------------------
# Name:        IO1Stuff
# Purpose:     Nota. Dah!
#
# Author:      Alguien con una mascara de Sujeto Fawkes
#
# Created:     19/09/1999
# Copyright:   (k) Ka-Tet Co. 1999-2019
# Licence:     <uranus>
#-------------------------------------------------------------------------------

def main():
    #Pruebas
    '''ejercicios para la clase'''
    print("Ejercicio clasico #1")
    #simplex([4,2],[[3,1],[-3,-1],[-4,-3],[1,2]],["<=","<=","<=","<="], [3,-3,-6,4],"Max") #Prueba maximizacion (https://www.programacionlineal.net/sensibilidad.html)
    print()
    print()
    print()
    print()
    print("Ejercicio clasico #2")
    #simplex([1,4,1,2],[[1,0,1,0],[2,1,0,1],[0,1,4,1]],["<=","<=","<="], [5,16,6],"Max") #Prueba maximizacion (http://gc.initelabs.com/recursos/files/r157r/w13108w/MateNegocios_unidad%203.pdf)
    print()
    print()
    print()
    print()
    print("Ejercicio aplicativo #1 (sobre granos en una empresa empaquetadora)")
    #simplex([5,6,5.5],[[1,1,1],[-2,1,-2],[0,0,1]],["<=","<=","<="], [100,0,30],"Max") #Prueba maximizacion (https://www.programacionlineal.net/sensibilidad.html)
    print()
    print()
    print()
    print()
    print("Ejercicio aplicativo #2 (sobre sillas, sillones y mecedoras)")
    #simplex([21,24,36],[[1,1,1],[1,1,2],[2,3,5]],["<=","<=","<="], [400,500,1450],"Max") #Prueba maximizacion (http://practicasprofesionales.ula.edu.mx/documentos/ULAONLINE/Licenciatura/Ing_ind_prod/PMI402/Semana%204/PMI402_S4_E_Ejem_met_Sim.pdf)
    simplex([20000,20000,20000,20000],[[2,1,1,2],[2,2,1,0],[0,0,2,2],[0,0,0,4]],["<=","<=","<=","<="], [24,20,20,16],"Max")
    #simplex([7,10],[[7,7],[10,5],[-2,7]], ["<=","==",">="], [20,10,5],"Max") #esta prueba es dos fases
    #simplex([4,6], [[2,1], [1,2], [1,1]], ["<=","<=","<="], [180,160,100], "Max") #Prueba maximizacion (cuaderno)
    #simplex([-5,-4], [[2,2], [6,3], [5,10]], ["<=","<=","<="], [14,36,60], "Min") #Prueba minimizacion (https://www.youtube.com/watch?v=BDA4_JsKedA)
    #simplex([2,7,-3], [[1,3,4], [1,4,-1]], ["<=","<="], [30,10], "Max") #Prueba minimizacion (https://www.programacionlineal.net/sensibilidad.html)
    #simplex([2,7,-3], [[1,3,4], [1,4,-1], [3,2,3]], ["<=","<=","<="], [30,10,25], "Max") #Prueba maximizacion (https://www.programacionlineal.net/sensibilidad.html)
    #simplex([0,0, 0,1],[[0,1, -1,0],[-1,1, 0,0],[1,-1, 0,0],[0,0, -1,1],[0,0, 1,-1]],["<=","<=","<=","<=","<="],[0,5,-5,8,-8], "Max") #Prueba minimizacion (http://www.phpsimplex.com/simplex/page2.php?o=min&x1=12.5&x4=15&x7=50&x10=20&x13=12.5&x19=10&x22=12&rt=27&v=27&l=es&r1_3=1&r1_5=-1&d1=-1&r2_6=1&r2_8=-1&d2=-1&r3_6=1&r3_11=-1&d3=-1&r4_12=1&r4_14=-1&d4=-1&r5_15=1&r5_17=-1&d5=-1&r6_18=1&r6_20=-1&d6=-1&r7_9=1&r7_23=-1&d7=-1&r8_21=1&r8_23=-1&d8=-1&r9_9=1&r9_26=-1&d9=-1&r10_1=1&r10_2=-1&r10_3=1&y10=5&r11_4=1&r11_5=-1&r11_6=1&y11=8&r12_7=1&r12_8=-1&r12_9=1&y12=12&r13_10=1&r13_11=-1&r13_12=1&y13=5&r14_13=1&r14_14=-1&r14_15=1&y14=6&r15_17=-1&r15_18=1&y15=3&r16_19=1&r16_20=-1&r16_21=1&y16=4&r17_22=1&r17_23=-1&r17_24=1&y17=3&r18_26=-1&r18_27=1&y18=1&r19_1=1&d19=-1&y19=2&r20_4=1&d20=-1&y20=2&r21_7=1&d21=-1&y21=3&r22_10=1&d22=-1&y22=1&r23_13=1&d23=-1&y23=2&r24_19=1&d24=-1&y24=2&r25_22=1&d25=-1&y25=1&r26_24=1&d26=-1&y26=30&r27_27=1&d27=-1&y27=30&Submit=Continuar)'''
    '''simplex([0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,1],
            [[0,1, -1,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,1, -1,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,1, 0,0, -1,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,1, -1,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,1, -1,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,1, -1,0, 0,0, 0,0],
            [0,0, 0,0, 0,1, 0,0, 0,0, 0,0, 0,0, -1,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,1, -1,0, 0,0],
            [0,0, 0,0, 0,1, 0,0, 0,0, 0,0, 0,0, 0,0, -1,0],
            [-1,1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [1,-1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, -1,1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 1,-1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, -1,1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 1,-1, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, -1,1, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 1,-1, 0,0, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, -1,1, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 1,-1, 0,0, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, -1,1, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 1,-1, 0,0, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, -1,1, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 1,-1, 0,0, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, -1,1, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 1,-1, 0,0],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, -1,1],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 1,-1],
            [0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,0, 0,1, 0,-1]],
            ["<=","<=","<=","<=","<=","<=","<=","<=","<=",
            "<=","<=","<=","<=","<=","<=","<=","<=","<=",
            "<=","<=","<=","<=","<=","<=","<=","<=","<=","<="],
            [0,0,0, 0,0,0, 0,0,0,
            5,-5,8,-8,12,-12,5,-5,6,-6,3,-3,4,-4,3,-3,1,-1,
            0], "Max") #Prueba minimizacion (http://www.phpsimplex.com/simplex/page2.php?o=min&x1=12.5&x4=15&x7=50&x10=20&x13=12.5&x19=10&x22=12&rt=27&v=27&l=es&r1_3=1&r1_5=-1&d1=-1&r2_6=1&r2_8=-1&d2=-1&r3_6=1&r3_11=-1&d3=-1&r4_12=1&r4_14=-1&d4=-1&r5_15=1&r5_17=-1&d5=-1&r6_18=1&r6_20=-1&d6=-1&r7_9=1&r7_23=-1&d7=-1&r8_21=1&r8_23=-1&d8=-1&r9_9=1&r9_26=-1&d9=-1&r10_1=1&r10_2=-1&r10_3=1&y10=5&r11_4=1&r11_5=-1&r11_6=1&y11=8&r12_7=1&r12_8=-1&r12_9=1&y12=12&r13_10=1&r13_11=-1&r13_12=1&y13=5&r14_13=1&r14_14=-1&r14_15=1&y14=6&r15_17=-1&r15_18=1&y15=3&r16_19=1&r16_20=-1&r16_21=1&y16=4&r17_22=1&r17_23=-1&r17_24=1&y17=3&r18_26=-1&r18_27=1&y18=1&r19_1=1&d19=-1&y19=2&r20_4=1&d20=-1&y20=2&r21_7=1&d21=-1&y21=3&r22_10=1&d22=-1&y22=1&r23_13=1&d23=-1&y23=2&r24_19=1&d24=-1&y24=2&r25_22=1&d25=-1&y25=1&r26_24=1&d26=-1&y26=30&r27_27=1&d27=-1&y27=30&Submit=Continuar)'''
    '''simplex([-1250,0,0,-1500,0,0,-500,0,0,-2000,0,0,-1250,0,0,0,0,0,-1000,0,0,-1200,0,0,0,0,0],
            [[0,0,1, 0,-1,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,1, 0,-1,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,1, 0,0,0, 0,-1,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,-1,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,-1,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,-1,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,-1,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,-1,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,-1,0],
            [1,-1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 1,-1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 1,-1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 1,-1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,-1,1, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,-1,1, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,-1,1, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,-1,1, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,-1,1],
            [1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,0,0, 0,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 1,0,0, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1, 0,0,0],
            [0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,0, 0,0,1]],
            ["<=","<=","<=","<=","<=","<=","<=","<=","<=",
            "<=","<=","<=","<=","<=","<=","<=","<=","<=",
            "<=","<=","<=","<=","<=","<=","<=","<=","<="],
            [0,0,0,0,0,0,0,0,0,
            5,8,12,5,6,3,4,3,1,
            2,2,3,1,2,2,1,30,30], "Min") #Prueba minimizacion (http://www.phpsimplex.com/simplex/page2.php?o=min&x1=12.5&x4=15&x7=50&x10=20&x13=12.5&x19=10&x22=12&rt=27&v=27&l=es&r1_3=1&r1_5=-1&d1=-1&r2_6=1&r2_8=-1&d2=-1&r3_6=1&r3_11=-1&d3=-1&r4_12=1&r4_14=-1&d4=-1&r5_15=1&r5_17=-1&d5=-1&r6_18=1&r6_20=-1&d6=-1&r7_9=1&r7_23=-1&d7=-1&r8_21=1&r8_23=-1&d8=-1&r9_9=1&r9_26=-1&d9=-1&r10_1=1&r10_2=-1&r10_3=1&y10=5&r11_4=1&r11_5=-1&r11_6=1&y11=8&r12_7=1&r12_8=-1&r12_9=1&y12=12&r13_10=1&r13_11=-1&r13_12=1&y13=5&r14_13=1&r14_14=-1&r14_15=1&y14=6&r15_17=-1&r15_18=1&y15=3&r16_19=1&r16_20=-1&r16_21=1&y16=4&r17_22=1&r17_23=-1&r17_24=1&y17=3&r18_26=-1&r18_27=1&y18=1&r19_1=1&d19=-1&y19=2&r20_4=1&d20=-1&y20=2&r21_7=1&d21=-1&y21=3&r22_10=1&d22=-1&y22=1&r23_13=1&d23=-1&y23=2&r24_19=1&d24=-1&y24=2&r25_22=1&d25=-1&y25=1&r26_24=1&d26=-1&y26=30&r27_27=1&d27=-1&y27=30&Submit=Continuar)'''
    #simplex([-3,-8], [[1,4], [1,2]], [-3.5,-2.5], "Min")
    #simplex([300,400], [[3,3],[3,6]], [120,180], "Max")
    #simplex([-180,-160],[[6,1],[3,1],[4,6]],[12,8,24], "mIn")
    #sixDual([-500,-600],[[-10,0],[-100,-200],[250,300]],[-100,-8000,15000], "Min")
    #sixDual([4,12,18],[[-1,0,-3],[0,-2,-2]],[3,5], "Max")
    #sixDual([315,110,50],[[-15,-2,-1],[-7.5,-3,-1],[-5,-2,-1]],[-200,-150,-120], "Min")
    #simplex([3,5],[[-1,0],[0,-2],[-3,-2]],[4,12,18],"MaX")

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

def simplex(Z: list, S: list, P: list, B: list, O: str):
    '''
        Moen consola
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
    #print("Entrada:", Z, S, P, B, O)
    if len(S) != len(P) or len(S)!=len(B):
        int("a")
    V = [f"X{i+1}" for i in range(len(Z))]
    #print("Entrada:", Z)
    I = []
    for i in range(len(P)):
        Z.append(0)
        if P[i] == "<=":
            for j in range(len(S)):
                S[j].append(0)
                if j == i:
                    S[j][-1] = 1
            V.append(f"S{i+1}")
            I.append(f"S{i+1}")
        elif P[i] == "==" or P[i] == "=":
            for j in range(len(S)):
                S[j].append(0)
                if j == i:
                    S[j][-1] = 1
            V.append(f"A{i+1}")
            I.append(f"A{i+1}")
        elif P[i] == ">=":
            for j in range(len(S)):
                S[j].append(0)
                if j == i:
                    S[j][-1] = -1
                S[j].append(0)
                if j == i:
                    S[j][-1] = 1
            V.append(f"S{i+1}")
            V.append(f"A{i+1}")
            I.append(f"A{i+1}")
            Z.append(0)
        else:
            Z.pop()
    for i in range(len(S)):
        S[i] = [float(j) for j in S[i]]
    Z = [float(i) for i in Z]
    B = [float(i) for i in B]
    nI = 0
    #print(f"Z {len(Z)} S {len(S)} P {len(P)} B {len(B)}")
    imprimirT(Z,V,S,B,nI,I)
    C = [i for i in Z]
    b = [i for i in B]
    A = [i for i in S]
    while True:
        T = iteracion(Z,S,B,O,V,I)
        Z = T[0]
        S = T[1]
        B = T[2]
        I = T[3]
        brk = True
        for i in Z:
            if O.upper() == "MIN":
                if i < 0:
                    brk = False
                    break
            if O.upper() == "MAX":
                if i > 0:
                    brk = False
                    break
        nI += 1
        imprimirT(Z,V,S,B,nI,I)
        if brk or nI >= len(Z):
            break
    print()
    print("Solucion:")
    for i in range(len(I)):
        print(f"    {I[i]}: {B[i]}")
    print()
    print("Analisis de Sensibilidad:")
    print("    Coeficientes Objetivo:")
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
        print(f"        {I[i]} puede tomar valores entre {limL} y {limR}.")
    print("    Recursos:")
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
        print(f"        El recurso {i} puede tomar valores entre {limL} y {limR}.")
        print(f"        El precio sombra del recurso {i} es de {PSi}.")

def iteracion(Z: list, S: list, R: list, O: str, V: list, I: list):
    print()
    comp = 0
    for i in Z:
        if abs(i) > abs(comp):
            if O.upper() == "MAX" and i > 0:
                comp = i
            elif O.upper() == "MIN" and i < 0:
                comp = i
    #print("Z Mayor:", comp)
    ind = Z.index(comp)
    #print("In-Columna:", ind)
    print(f"Entra {V[ind]}", end=" y ")
    comp = 99999999
    for i in range(len(R)):
        if S[i][ind] > 0 and abs(R[i]/S[i][ind]) < abs(comp):
            comp = R[i]/S[i][ind]
            out = i
    #print("R Menor:", comp)
    #print("Out-Fila:", out)
    print(f"sale {I[out]}")
    R[out] = R[out]/S[out][ind]
    S[out] = [i/S[out][ind] for i in S[out]]
    for i in range(len(S)):
        if i != out:
            R[i] = R[i]-S[i][ind]*R[out]
            S[i] = [S[i][j]-S[i][ind]*S[out][j] for j in range(len(S[i]))]
    Z = [Z[j]-Z[ind]*S[out][j] for j in range(len(Z))]
    I[out] = str(V[ind])
    print()
    return (Z,S,R,I)

if __name__ == '__main__':
    main()
