# Tarea 1: DCCapitollio


## Consideraciones generales :octocat:

* El código en general cumple con lo pedido, al entrar existe el menú principal que presenta las opciones de iniciar la partida o salir del programa. El menú principal y la simulación de juego presentan lo mínimo en el ambito de las opciones de acciones. Además tiene las opciones salir, con lo cual se cierra el juego y volver donde se retrocede al menú o acción anterior.

* En el menú principal se pueden realizar todas las opciones en una cantidad infinita de veces hasta ser elegida la simulación de hora. En la cual tras escoger una acción ,y esta sea posible de desarrollar, se llevan a cabo los eventos de la hora. Es decir los encuentros, cantidad definida por la fórmula según el nivel del escenario escogido. El evento, que tiene una probabilidad de ocurrir. Y un resumen con la información de la hora.

* El juego termina si es que el tributo muere, en tal caso termina de ocurrir la simulación de hora y se muestra el resumen de hora. Tras lo cual se informa que fue derrotado y se elige un tributo a azar para ser seleccionado como ganador. También puede terminar si es que no quedan más tributos con vida, en cuyo caso se informa que fue el ganador del juego. En ambas opciones se vuelve al menú principal para decidir salir o volver a jugar.

* Todos los inputs son a prueba de errores, por lo cual el programa no debería caerse o cerrarse a menos que se le indique con la opción salir. 

* Todos los parámetro utilizados se encuentran en el archivo parámetros, por lo cual es fácil modificar alguno de ellos si es que se quiere aumentar o disminuir la dificultad.


### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos: 38 pts (27%)
##### ✅ Diagrama <explicacion\>
##### ✅ Definición de clases, atributos y métodos <explicacion\>
##### ✅ Relaciones entre clases <Las clases abstractas se encuentran en la línea 5 del archivo ambiente y en la línea 5 del archivo objeto>
#### Simulaciones: 12 pts (8%)
##### ✅ Crear partida <Se instancian los objetos de las clases en el archivo lectura_archivos>
#### Acciones: 43 pts (30%)
##### ✅ Tributo <Además de las funciones obligatorias, cree la función atacar_encuentros, que es el ataque que realizan los tributos en los encuentros. De esta manera no gastan energía, ni aumentan su popularidad si es que el tributo atacado muere>
##### ✅ Objeto <explicacion\>
##### ✅ Ambiente <El daño respectivo según el tipo de ambiente se ve al utilizar una funcion abstracta, línea 12, archivo ambiente>
##### ✅ Arena <Además de las acarcterísticas obligatorias se creó muertos, donde se almacenan los tributos que murieron en la última hora, informacion_hora donde se almacena el resumen y ambiente_turno donde se guarda el tipo de ambiente que hay en la hora. También se agregaron funciones extras, entregar jugador y ambientes, las cuales guardan información. Eventos_fin_hora. Encargada de realizar todos los eventos al final de una simulación de hora, y siguiente ambiente, que cambia la variable ambiente_turno. Los encuentros por turno, se basan en una fórmula que se encuentra en la línea 34 del archivo arena>
#### Consola: 34 pts (24%)
##### ✅ Menú inicio <explicacion\>
##### ✅ Menú principal <explicacion\>
##### ✅ Simular Hora <Las acciones de la simulacion de hora se llaman desde el archivo DCCapitolio. La acción heroica se encuentra en la línea 133 del archivo tributo, atacar tributo se encuentra en la línea 48 del archivo tributo, pedir objeto se encuentra en la línea 108 del archivo tributo, y hacerse bolita se encuentra en la línea 151 del archivo tributo. Los encuentros entre tributos, el evento y el resumen se encuentran en la línea 64 del archivo arena >
##### ✅ Robustez <explicacion\>
#### Manejo de archivos: 15 pts (11%)
##### ✅ Archivos CSV  <explicacion\>
##### ✅ parametros.py <explicacion\>
#### Bonus: 3 décimas máximo
##### ❌ Guardar Partida <explicacion\>

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```ambiente.py``` en ```Tarea 1```
2. ```arena.py``` en ```Tarea 1```
3. ```dccapitolio.py``` en ```Tarea 1```
4. ```lectura_archivos.py``` en ```Tarea 1```
5. ```objeto.py``` en ```Tarea 1```
6. ```parametros.py``` en ```Tarea 1```
7. ```tributos.py``` en ```Tarea 1```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```abc```: ```abstractmethod() / ABC```
2. ```random```: ```randint```
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```ambiente```: Contiene a la clase abstracta ```Ambiente``` y las clases que heredan de ella ```Playa```, ```Bosque```, ```Montana```
2. ```arena```: Contiene a la clase ```Arena```
3. ```objeto```: Contiene a la clase abstracta ```Objeto``` y las clases que heredan de ella ```Consumible```, ```Arma```, ```Especial```
4. ```tributo```: Contiene a la clase ```Tributo```
5. ```dccapitolio```: Contiene a la clase ```DCCapitolio```
5. ```Parametros```: Hecha para <Contener los párametros y de esta forma poder modificarlos>
6. ```Cargar archivos```: Hecha para <Cargar la información de los archivos en 4 listas distintas>

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Existen infinitas copias de un objeto, esto en base de que fuera de la arena los patrocinadores pueden conseguir una nueva unidad del mismo objeto> 
2. <Volver al menú principal implica reiniciar el juego 2, este supuesto lo adopte dado que no encuentro que tenga sentido volver al menú principal si es que no se quiere cambiar de tributo u arena, y para ello es importante reiniciar la partida para que no existan problemas con la información de los tributos. Por ejemplo su ingenio, fuerza, vida, entre otros>
3. <La probabilidad de un evento es de un 50% según el código utilizado, esto para tener una opción media de ocurrencia. Sin que provoque una gran o pequeña cantidad de daño>

-------


## Referencias de código externo :book:

Para realizar mi tarea saqué código de: No fue utilizado codigo externo
1. \< https://github.com/IIC2233/Syllabus/tree/main/Actividades/AF3>: este hace \<es la actividad formativa 3 realizada en clases> y está implementado en el archivo <main.py> en las líneas <3-5> y hace <Es la estructura de inicio del programa que se utilizo como base en este codigo>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
