import interfaz as gui

def esFactible (fila,solucion):
    for x in range(fila):
        if(solucion[x]==solucion[fila] or abs(fila-x)== abs(solucion[fila]-solucion[x])):
            return False
    return True

def reinas (solucion,fila,nreinas):
    exito=False;
    if fila<nreinas:
        while(solucion[fila]<nreinas-1 and not exito):
            solucion[fila]=solucion[fila]+1
            if(esFactible(fila,solucion)):
                exito=reinas(solucion,fila+1,nreinas)
        if(not exito):
            solucion[fila]=-1
    else:
        gui.reinas(solucion,0)
        exito=True

    return exito

