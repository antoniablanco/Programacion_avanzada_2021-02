# Tarea 3: DCCalamar:

* El código no cumple con todo lo pedido, se realizó la encriptación, separación cliente/servidor, backend/frontend y se creo el networking. Es capas de mandar mensajes entre el cliente y el servidor, los cuales van encriptados y codificados según los pedido. En la ventana de inicio se verifica las condiciones del nombre y la fecha, tras lo cual pasa a la ventana de espera. Al unirse nuevos clientes al servidor esta ventana se actualiza automaticamente. 

* Es posible retar a otro jugador, al realizar esta accion ambos jugadores no podran retar ni ser retados. A quien se le envio la invitacion, se le traslada a una ventana de reto donde elige si aceptar o rechazar este. Si es que lo rechaza se vuelve a la sala principal, pudiendo retar y ser retados nuevamente. Si es que aceptar el reto ambos jugadores pasan a la sala de juego. El juego no fue implementado, pero los botones de la ventana son apretables y cumplen con las dimensiones pedidas, es decir solo puede apostar el maximo de canicas que posee. Al apretar el boton listo se pasa a la ventana final, siendo el ganador quien eligio el juego. 

* En esta última ventana es posible apreciar al jugador ganador y perdedor. Si es que se elige jugar una nueva partida se vuelve a la ventana de inicio, eliminando los datos del cliente.

* En caso de desconexion del cliente el servidor avisa a traves de un log y cierra su socket, si es que fue el servidor quien se desconecto, se avisa a todos los jugadores y se cierra el programa.

* Los parametros se encuentran como archivos json, uno para el cliente y otro para el socket. Se crea una funcion que lee y obtiene estos valores.

## Consideraciones generales :octocat:

<No se implemento el juego perse, por lo cual no hay apuestas, cambio de turno ni verificacion si es que un jugador gano, por lo mismo no existen logs asociados a estas acciones.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 23 pts (18%)
##### ✅ Protocolo <El port y host se encuentra en parametros, >
##### ✅ Correcto uso de sockets <Los sockets se instancian en los archivos servidor/servidor1.py y cliente/cliente1.py. Al crearse un thread para cada cliente no se bloquean>
##### ✅ Conexión <explicacion\>
##### ✅ Manejo de clientes <explicacion\>
#### Arquitectura Cliente - Servidor: 31 pts (24%)
##### ✅ Roles <Todo el funcionamiento del cliente se encuentra en la carpeta cliente y el del servidor en la carpeta servidor>
##### ✅ Consistencia <Se utilizan locks en distintas acciones tomadas por el servidor estas se pueden ver en el archivo servidor1.py linea 127 y en el archivo logica_juego implementado en la linea 59 al eliminar a un cliente, linea 83 al ingresar un cliente, 104 al actualizar los clientes que pueden ser retados, 112 al retar a un jugador, 142 al rechazar un reto>
##### ✅ Logs <explicacion\>
#### Manejo de Bytes: 20 pts (15%)
##### ✅ Codificación <La codificacion del servidor se encuentra en el archivo servidor1 entre las lineas 105 y 121, en el caso del cliente esta en el archivo cliente1 lineas 36 a la 62>
##### ✅ Decodificación <La decodificacion del servidor esta en el archivo servidor1 lineas: 60 a la 95, para el cliente esto se encuentra en el archivo cliente1 entre las lineas 77 a las 111>
##### ✅ Encriptación <La encriptacion y desincriptacion se encuentra en los archivos codificacion.py tanto del servidor como del cliente>
##### ✅ Integración <El protocolo de envio se puede observar para el servidor en el archivo servidor1 en las lineas 97 a la 103 y para el cliente, en el arcivo cliente1 lineas 36 a la 42>
#### Interfaz gráfica: 31 pts (24%)
##### ✅ Modelación <La separacion del frontend y backend se puede observar en los archivos que componen las carpetas de los mismos nombres, dentro de la carpeta cliente>
##### ✅ Ventana inicio <explicacion\>
##### ✅ Sala Principal <explicacion\>
##### ✅ Ventana de Invitación <explicacion\>
##### 🟠 Sala de juego <No se implemento los resultados de ronda, que la ronda se acabe al obtener 20 canicas>
##### ✅ Ventana final <explicacion\>
#### Reglas de DCCalamar: 21 pts (16%)
##### ✅ Inicio del juego <explicacion\>
##### ❌ Ronda <explicacion\>
##### ❌ Termino del juego <explicacion\>
#### General: 4 pts (3%)
##### ✅ Parámetros (JSON) <explicacion\>
#### Bonus: 5 décimas máximo
##### ❌ Cheatcode <explicacion\>
##### ❌ Turnos con tiempo <explicacion\>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```servidor/main.py y cliente/main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```parametros.json``` en ```servidor```
2. ```parametros.json``` en ```cliente```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```threading```: ```Lock, Thread```
2. ```random```: ```randint```
3. ```json```: ```load```
4. ```os```: ```path```
5. ```socket```: ```socket```
6. ```PyQt5```: ```QtCore```
7. ```PyQt5```: ```QtWidgets```
8. ```PyQt5```: ```QtGui```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```obtener_parametros```: Contiene a ```parametro```, ```ruta```, 
2. ```codificacion```: Contiene a ```encriptacion```, ```desincriptacion```
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Al apretar el boton listo de la sala juego se pasa a la ventana final> 
2. <Cuando un jugador reta a otro se mantiene en la sala de espera pero sin poder apretar botones>
3. <Para evitar un loop infinito, si es que se manda un mensaje entre servidor-cliente que no se puede decodificar, se cierra el socket del cliente>

PD: <Es importante saber que las ventanas aparecen todas en la misma posicion, por lo cual si es que uno tiene mas de un cliente en la misma pantalla, al realizar un cambio de ventana de uno de los clientes si es que para el otro cliente no se movio su ventana. La nueva ventana aparecera atras de la ya existen. Por ello hay que mover las ventanas para poder visualizarlas todas.>


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://www.delftstack.com/es/howto/python/python-invert-a-dictionary/>: este hace \<Cambia las keys por los values en un diccionario> y está implementado en el archivo <sala_principal.py> en las líneas <129> y hace <intercambia el diccionario de nombres y ids de los juhadores>
2. \<Se utilizo como codigo base la ayudantia 7.5, la actividad formativa 4 y el ejemplo de networking>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
