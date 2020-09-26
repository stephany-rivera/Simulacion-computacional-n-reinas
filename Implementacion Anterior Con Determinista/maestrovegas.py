##########################################
# Taller 3 - Simulación Computacional    #
# Stephany Rivera Guzmán                 #
# Santiago Romero Andrade                #
# Laura María Tascón Vasco               #
##########################################

#  -*- coding: utf-8 -*-
import random as rd
import sys
import interfaz as gui

n_reinas=0
nreinas_faltantes=0
posiciones_reinas=0
solucion =[]
comprobar = []
run=0
i=0
inicio=0
exito=True
reinascolocadasmal=0

# Funcion principal que agrega las reinas de la manera en que se comporta un algoritmo las vegas
def maestro(gui_nreinas):
    global solucion,exito,nreinas_faltantes,comprobar,i,n_reinas,posiciones_reinas,reinascolocadasmal
    nreinas_faltantes=gui_nreinas
    n_reinas=gui_nreinas
    posiciones_reinas=rd.sample(range(0,n_reinas), n_reinas)
    while True:
            if(exito==False):
                comprobar.clear()
                solucion.clear()
                print("fallo")
                reinascolocadasmal+=n_reinas-nreinas_faltantes
                exito=True
                reiniciar()
            elif(nreinas_faltantes == 0):
                if(run!=0):
                    gui.reinas(solucion,reinascolocadasmal/run)
                else:
                    gui.reinas(solucion,0)
                break
            nreinas_faltantes -= 1
            columna_reina = posiciones_reinas[i]
            solucion.append(columna_reina)
            print(solucion)
            verificar_diagonales(i, columna_reina, 0)
            verificar_diagonales(i, columna_reina, 1)
            i += 1

# Funcion que verifica los dos tipos de diagonales que se deben tener en cuenta con el arreglo de reinas cada vez que se agrega
def verificar_diagonales(posi_fila,posi_columna,angulo):
    global comprobar,solucion,exito
    while posi_fila>0:
        if(angulo==0):#diagonal 45
            posi_columna-=1
        if(angulo==1):#diagonal 135
            posi_columna+=1
        posi_fila-=1
        comprobar.append(posi_columna)
    comprobar.reverse()
    print(comprobar,"comprobar angulo",angulo)
    for x in range(len(comprobar)):
        item_a = solucion[x]
        item_b = comprobar[x]
        if (item_a == item_b):
            exito=False
            break
    comprobar.clear()

# Funcion que reinicia las variables para empezar un nuevo intento
def reiniciar():
    global nreinas_faltantes,run,i,posiciones_reinas
    posiciones_reinas=rd.sample(range(0,n_reinas), n_reinas)
    nreinas_faltantes = n_reinas
    i=0
    run+=1
    print("-------------",run,"---------------")






