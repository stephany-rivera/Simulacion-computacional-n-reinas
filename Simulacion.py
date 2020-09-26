######################################
# Santiago Romero Andrade - 1765512 ##
# Stephany Rivera Guzmán - 1765591  ##
# Laura María Tascón Vasco - 1765534##
######################################

#enconding: utf-8
import random
import simpy
import numpy as np
import pandas as pd

SEMILLA = 42
DURACION_SIMULACION = 28800  # Tiempo de la simulación en segundos
COLA = 0
COLAMAXIMA = 0
CANTIDAD_COLAS=0
COLA_ACUMULADA=0
ESPERA_ROBOTS = np.array([])
#llegada
media=4
nreinas=0
#algunas variables de desempeño
tiempoServicio = 0
totalUtilidadHumano = 0
totalUtilidadYo = 0
total_humano_gana = 0
total_robot_gana = 0
total_jugadas = 0
tiempo_tiempo_servicio = 0
total_tiempo_servicio = 0
tiempoRobot = 0
tiempoHumano = 0

# Funcion que calcula el tiempo de servicio basado en las distribuciones de los robot para resolver el algoritmo y el tiempo del humano dependiendo de la cantidad de reinas
def tiempo_servicio():
    global tiempoServicio,total_tiempo_servicio,total_robot_gana,total_humano_gana,totalUtilidadHumano,totalUtilidadYo,nreinas
    numeros=[4,5,6,8,10,12,15]
    prob=[1/7,1/7,1/7,1/7,1/7,1/7,1/7]
    nreinas=np.random.choice(numeros, 1, p=prob)
    print("---- Se juega con -----",nreinas,"reinas ----")
    if(nreinas==[4]):
        tiempoRobot = np.random.uniform(0.026984, 0.2168670)
        tiempoHumano = 0.311
    elif(nreinas==[5]):
        tiempoRobot = np.random.uniform(0.0229850, 0.1637468)
        tiempoHumano = 0.428
    elif(nreinas==[6]):
        tiempoRobot = np.random.uniform(0.2428603, 1.3525548)
        tiempoHumano = 0.460
    elif(nreinas==[8]):
        tiempoRobot = np.random.uniform(0.2032099, 1.7262332)
        tiempoHumano = 0.492
    elif(nreinas==[10]):
        tiempoRobot = np.random.uniform(1.3734701, 30.4734795)
        tiempoHumano = 0.510
    elif(nreinas==[12]):
        tiempoRobot = np.random.uniform(4.7870877, 126.9911666)
        tiempoHumano = 0.533
    else:
        tiempoRobot = np.random.uniform(23.7112496, 861.8304920)
        tiempoHumano = 0.574

    if(tiempoRobot>tiempoHumano):
        tiempoServicio=tiempoHumano
        total_tiempo_servicio += tiempoServicio
        total_humano_gana+=1
        totalUtilidadHumano+=15
        totalUtilidadYo+=15
    else:
        tiempoServicio=tiempoRobot
        total_tiempo_servicio += tiempoServicio
        total_robot_gana+=1
        totalUtilidadYo-=10

# Funcion que utiliza los tiempos de servicios y que ocupa al humano con el robot
def robot(env, name, humano):
    global COLA,COLAMAXIMA,CANTIDAD_COLAS,COLA_ACUMULADA,ESPERA_ROBOTS
    print('%s llega a las  %.1f' % (name, env.now), "| Cola actual:",COLA)
    llegada = env.now
    if(COLA!=0):
        COLA_ACUMULADA+=COLA
        CANTIDAD_COLAS+=1
    COLA += 1        
    with humano.request() as req:
        if COLA > COLAMAXIMA:
            COLAMAXIMA = COLA
        yield req
        espera = env.now - llegada
        ESPERA_ROBOTS = np.append(ESPERA_ROBOTS, espera)
        print('%s comienza la atención en %s' % (name, np.round(env.now,2)))
        COLA = COLA - 1
        tiempo_servicio()
        yield env.timeout(tiempoServicio)
        print('%s termina su atención a las %s' % (name, np.round(env.now,2)))

# Funcion que determina las llegadas de los robots basadas en una distribucion uniforme y termina cuando sean las 8 horas
def llegada(env, humano):
    i = 1
    while env.now<=DURACION_SIMULACION:
        c = robot(env, 'Robot %d' % i, humano)
        global total_jugadas
        total_jugadas += 1
        env.process(c)
        tiempo_llegada = np.random.uniform(5, 10)
        yield env.timeout(tiempo_llegada)
        i += 1

# Funcion que da inicio a la simulacion
def inicio():
    print('JUEGO N REINAS')
    random.seed(SEMILLA)
    np.random.seed(SEMILLA)
    env = simpy.Environment()
    servidor = simpy.Resource(env, capacity=2)
    env.process(llegada(env, servidor))
    env.run()

inicio()
print("---------------------------------------------------------------")
print("UTILIDAD")
print("Total Utilidad Mia:", totalUtilidadYo)
print("Total Utilidad Humano:", totalUtilidadHumano)
print("TOTAL:", totalUtilidadYo+totalUtilidadHumano)
print("---------------------------------------------------------------")
print("JUEGOS")
print("Veces que gana humano:", total_humano_gana)
print("Veces que gana robot:", total_robot_gana)
print("TOTAL:", total_jugadas)
print("---------------------------------------------------------------")
print("PROMEDIOS")
print("Tiempo promedio de atención por robot:", np.round(total_tiempo_servicio/total_jugadas,2), "segundos")
if(CANTIDAD_COLAS==0):
    print("Tamaño promedio de la cola:",0,"robots")
else:
    print("Tamaño promedio de la cola:",np.round(COLA_ACUMULADA/CANTIDAD_COLAS,2),"robots")
print("Tiempo promedio de espera:",np.round(np.mean(ESPERA_ROBOTS),2),"segundos")
print("Tamaño máximo de la cola:",COLAMAXIMA,"robots")
