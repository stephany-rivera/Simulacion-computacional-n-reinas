# PROYECTO SIMULACIÓN COMPUTACIONAL: "El maestro del ajedrez" 
## Simulación de la solución del problema de las n reinas mediante el algoritmo las vegas y el algoritmo determinista:crown:
### Summary
Dos personas deciden montar una idea de negocio donde una de ellas juega el juego de las n reinas con un robot. Si el humano 
gana obtiene 30 y son 15 para cada persona y si el robot gana, la persona que no jugó pierde 10. Se realiza una simulación donde 
se busca saber que ganancia obtiene la persona que no juega según la siguiente disposición:

##### Datos de la simulación :clipboard:
* Siempre juega la misma persona contra el robot.
* Los robots llegan de acuerdo a una distribución uniforme entre 10  y 30 segundos.
* El robot soluciona el problema de acuerdo con el algoritmo las vegas.
* La persona soluciona el problema de acuerdo con el algoritmo determinista.
* Cuando va iniciar el juego, el robot y el humano seleccionan el tablero de acuerdo a una distribución uniforme. Los posibles<br />
valores de n son 4,5,6,8,10,12 y 15.
* El que solucione el problema en un tiempo menor en cada partida gana.
* La simulación tiene una duración de 8 horas.

##### Ejecución :gear:

* La ejecución del archivo ```Simulacion.py``` ejecuta la simulación del programa y muestra que sucede en cada partida y al final <br />
cuando se completa el tiempo de la simulación muestra cuanta utilidad generaron las personas, cuantos juegos ganó el humano y cuantos <br />
el robot y los promedios en tiempo de atención y de espera de los robots. 

* La ejecucion del archivo ```main.py" ``` permite mostrar la interfaz gráfica de como se soluciona el juego de las n reinas ya sea mediante <br />
el algoritmo de las vegas o el algoritmo determinista según la elección del usuario. Además, muestra el tiempo que demora en encontrar la solución <br />
y número de intentos promedios antes de tener éxito. 
<br /> <br />

 ***Se hizo uso del lenguaje de programación PYTHON :snake:.***

