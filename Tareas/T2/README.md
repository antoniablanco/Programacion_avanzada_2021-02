# Tarea 2: DCCrossy Frog:


* El código en general cumple con lo pedido, desde la ventana inicio se puede acceder a la vetnana ranking donde se presentan los primero 5 puntajes en orden descendente. Desde esta ventana se retrocede a la ventana de inicio a traves del boton volver o del boton cerrar. También se puede proseguir a la ventana de juego desde la ventana inicio, ingresando un nombre y qe este cumpla con las caracteristicas pedidas.

* En el juego se tiene dos areas de autos y un area de rio, cada un tiempo especifico aparecen objetos especiales que al ser agarrados entregan un efecto, el cual fue implementado. En el rio solo se puede saltar hacia adelante o atras, y al quedar en un tronco se mueve con el. No fue implementado el movimiento caminar sobre el tronco. El movimiento de salto se da con la tecla "j" del teclado.
En esta ventana se muestran actualizadamente las estadisticas. Ademas, se tiene el boton salir que lleva a la ventana de inicio dando la posibilidad de comenzar un nuevo juego. Y también se tiene el boton pausar, el cual detiene el juego y con ello los personajes, el tiempo, los objetos y la posibilidad de movimiento. Es posible pausar con la tecla p. El juego termina al acabarse las vidas, el tiempo o llegar a la meta, tras lo cual se prosigue a la ventana post nivel.

* La ventana post nivel presenta las estadisticas del nivel terminado, y dependiendo si es que puede seguir jugando o no se da la posiblidad de siguiente nivel. Al apretar el boton salir se vuelve a la pantalla de inicio. 

* Todos los parámetro utilizados se encuentran en el archivo parámetros, por lo cual es fácil modificar alguno de ellos si es que se quiere modificar las variables.

* Se implemento el bonus de musica, el cual reinicia la cancion entregada al abrir cada ventana y se pausa al pausar el juego. También fue implementado el bonus check point, se tiene dos puntos de descanso uno entre la carretera y el rio y el otro entre el rio y la otra carretera.


## Consideraciones generales :octocat:

<No se implemento el movimiento de caminar en el tronco, y los objetos aparecen en un lugar al azar del mapa sin contar el rio y la meta, por lo cual si pueden suporponerse. >

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventana de Inicio: 4 pts (3%)
##### ✅ Ventana de Inicio <explicacion\>
#### Ventana de Ranking: 5 pts (4%)
##### ✅ Ventana de Ranking <Las funciones para mostrar los cinco mejores puntajes estan en la linea 60 del archivo frontend/ventana_ranking.py, la apertura y orden de estos datos se ve en el archivo backend/logica_ranking linea 15>
#### Ventana de juego: 13 pts (11%)
##### ✅ Ventana de juego <explicacion\>
#### Ventana de post-nivel: 5 pts (4%)
##### ✅ Ventana post-nivel <explicacion\>
#### Mecánicas de juego: 69 pts (58%)
##### ✅ Personaje <explicacion\>
##### ✅ Mapa y Áreas de juego <El aumento de la velocidad de los autos se calcula en la linea 218 del archivo backend/logica_juego.py, con este se actualiza la variable de clase que guarda las velocidades de los autos y troncos.
El sentido de los autos es aleatorio, esto se ve en la linea 57 del archivo backend/logica_juego.py, en el cual a partir de un randint se elige el sentido de la linea.
El sentido de los troncos es aleatorio y se ve en la linea 80, utiliza el mismo funcionamiento de los autos>
##### ✅ Objetos <Los objetos aparecen cada un tiempo especifico, este codigo se encuentra en la linea 131 del archivo backend/logica_juego.py, en la cual se llama a la funicon que instancia los objetos>
##### ✅ Fin de Nivel <El puntaje del turno se calcula en la linea 205 del archivo backend/logica_juego.py>
##### ✅ Fin del juego <El puntaje total se guarda en el archivo puntajes.txt al acabar el juego, el codigo de esto se encuentra en la linea 20 del archivo backend/logica_post.py>
#### Cheatcodes: 8 pts (7%)
##### ✅ Pausa <explicacion\>
##### ✅ V + I + D <explicacion\>
##### ✅ N + I + V <explicacion\>
#### General: 14 pts (12%)
##### ✅ Modularización <explicacion\>
##### ✅ Modelación <explicacion\>
##### ✅ Archivos  <explicacion\>
##### ✅ Parametros.py <explicacion\>
#### Bonus: 10 décimas máximo
##### ❌ Ventana de Tienda <explicacion\>
##### ✅ Música <explicacion\>
##### ✅ Checkpoint <explicacion\>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```parametros.py``` en ```frontend```
2. ```puntajes.txt``` en ```T2```

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```QtCore```
2. ```PyQt5```: ```QtWidgets```
3. ```PyQt5```: ```QtGui```
4. ```PyQt5```: ```QtMultimedia```
5. ```Random```: ```randint```
5. ```Random```: ```choice```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ventana_inicio``` en ```frontend```
2. ```ventana_juego``` en ```frontend```
3. ```ventana_post``` en ```frontend```
4. ```ventana_ranking``` en ```frontend```
5. ```logica_inicio``` en ```backend```
6. ```logica_juego``` en ```backend```
7. ```logica_post``` en ```backend```
8. ```logica_ranking``` en ```backend```
9. ```Troncos``` en ```backend\clases_objetos.py```
10. ```Autos``` en ```backend\clases_objetos.py```
11. ```Objeto``` en ```backend\clases_objetos.py```
12. ```Frogg``` en ```backend\clases_objetos.py```
13. ```Musica``` en ```backend\clases_objetos.py```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Al apretar el boton salir se vuelve a la pagina inicio, de esta forma se tiene la oportunidad de comenzar de nuevo> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...


-------

Para realizar mi tarea saqué código de:
1. \<http://pythonlcpa.blogspot.com/p/blog-page_75.html>: este hace \<Implementa un pop up de pregunta > y está implementado en el archivo <ventana_juego> en las líneas <311-324> y hace <Pausa la pantalla y pregunta si es que se quiere seguir pausado o salir del juego>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
