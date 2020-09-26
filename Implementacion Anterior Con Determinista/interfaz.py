#  -*- coding: utf-8 -*-
import maestrovegas
import determinista
import sys
from functools import partial
import time
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
except ImportError:
    import tkinter.ttk as ttk

ene=None
root=None
nreinas=0
solucion=None
promedioreinas=0
tipodealgoritmo=False
combo=None
# Funciones para dar inicio y continuidad a las interfaces
def vp_start_gui():
    global w,root
    root = tk.Tk()
    root.resizable(False, False)
    top = todo (root)
    init(root, top)
    root.mainloop()

def init(top, gui, *args, **kwargs):
    global w
    w = gui
    top_level = top
    root = top

def init2(top, gui, *args, **kwargs):
    global w, root
    w = gui
    top_level = top
    root = top

def vp_start_gui2():
    global w, root
    root = tk.Tk()
    root.resizable(False, False)
    top = cuadro (root)
    init(root, top)
    root.mainloop()

w = None

def destroy_todo():
    global w
    w.destroy()
    w = None

#Click al primer botón
def what():
    global nreinas
    global combo
    nreinas=int(ene.get())
    root.destroy()
    if(combo.get()==True):
        start = time.time()
        maestrovegas.maestro(nreinas)
        end = time.time()
    else:
        solucion=[0]*nreinas
        start = time.time()
        determinista.reinas(solucion,0,nreinas)
        end = time.time()
    print("Tiempo:",(end - start)*1000,"milisegundos")
    vp_start_gui2()
    
# Funcion que imprime la solucion (llamada desde maestrovegas)
def reinas(sol,promedio):
    global solucion,promedioreinas
    solucion=sol
    promedioreinas=promedio
    print(sol,"<-Esta es la sol")
    print("Promedio de reinas colocadas hasta fallar:",promedio)

#Clase inicial de interfaz
class todo:
    def __init__(self, top=None):
        global ene
        global combo
        top.geometry("120x170")
        top.title("")
        top.iconbitmap(default="img/corona.ico")

        self.ene = tk.Spinbox(values=(4,5,6,8,10,12,15))
        self.ene.place(relx=0.167, rely=0.25,height=40, relwidth=0.333)
        self.ene.configure(state='readonly')
        ene=self.ene

        self.go = tk.Button(top)
        self.go.place(relx=0.5, rely=0.25, height=40, width=40)
        self.go.configure(command=what)
        self.go.configure(text='''GO''')

        self.titulo = tk.Label(top)
        self.titulo.place(relx=0.25, rely=0.0, height=19, width=50)
        self.titulo.configure(text='''N Reinas''')

        combo = tk.BooleanVar(top)
        self.check = tk.Checkbutton(top, variable=combo)
        self.check.configure(text='Vegas ON')
        self.check.place(relx=0.167, rely=0.55, height=25, width=80)

#Clase de interfaz del tablero de ajedrez
class cuadro:
    def __init__(self, top=None):
        self.reinas=  [[0 for x in range(nreinas)] for x in range(nreinas)]
        self.fondo1 = tk.PhotoImage(file="img/uno.png")
        self.fondo2 = tk.PhotoImage(file="img/dos.png")
        self.reina1 = tk.PhotoImage(file="img/reinablanca1.png")
        self.reina2 = tk.PhotoImage(file="img/reinablanca2.png")

        top.geometry("{}x{}".format(nreinas*40,nreinas*40))
        top.title("N Reinas - Simulación")
        if(nreinas%2==0):
            color=False
        else:
            color=True
        
        # Ciclo de creacion de Labels para el tablero 
        for x in range(nreinas):
            if(nreinas%2==0):
                if(color==True):
                    color=False
                else:
                    color=True
            for y in range(nreinas):
                self.reinas[x][y] = tk.Label(top,borderwidth=0)
                if(color==True):
                    self.reinas[x][y].place(x=40*x, y=40*y, height=40, width=40)
                    self.reinas[x][y].configure(image=self.fondo1)
                    color=False
                else:
                    self.reinas[x][y].place(x=40*x, y=40*y, height=40, width=40)
                    self.reinas[x][y].configure(image=self.fondo2)
                    color=True
        equis=0
        ### Ciclo que dibuja la solución en el tablero
        for i in solucion:
            if(self.reinas[equis][i].cget("image")=='pyimage1' or self.reinas[x][y].cget("image")=='pyimage3'):
                self.reinas[equis][i].config(image=self.reina1)
            else:
                self.reinas[equis][i].config(image=self.reina2)
            equis+=1