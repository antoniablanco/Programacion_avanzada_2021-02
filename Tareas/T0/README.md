# Tarea 0: DCCommerce

## Consideraciones generales :octocat:
* El código en general cumple con lo pedido, al entrar existe la opcion de ingresar a una cuenta ya existente, crear una cuenta, entrar anonimamente o salir del programa. Dependiendo de en cual de estas opciones uno entre se podrán crear publicaciones, eliminar publicaciones creadas por el usuario o agregar comentarios a otras publicaciones. En todos los menues existe la opción de volver al menú anterior. Al desplegar las publicaciones estan se encuentran de forma decendente y los comentarios asociados a una en forma ascendente.

* Al eliminar una publicación se eliminan los comentarios que este tenía. No existe una opción para eliminar una cuenta. En el programa se manipulan los archivos entregados, por lo cual se puede crear una publicación, cerrar el programa y apagar el computador. Y al volver a entrar existirá esta publicación. 

* En todas las pruebas hechas, el programa fue aprueba de errores. Es decir al entregar inputs que no son opciones tanto de numero o palabras el programa no tiene problemas y vuelve a pedir las respuestas. En todos los casos entregando un mensaje que especifica el error. Aunque dependiendo del tamaño de la ventana donde se ve el output este mensaje puede quedar muy arriba y no verse.

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Menú de Inicio (14pts) (14%)
##### ✅ Requisitos
##### ✅ Iniciar sesión
##### ✅ Ingresar como usuario anónimo
##### ✅ Registrar usuario
##### ✅ Salir
#### Flujo del programa (35pts) (35%) 
##### ✅ Menú Principal
##### ✅ Menú Publicaciones
##### ✅ Menú Publicaciones Realizadas
#### Entidades 15pts (15%)
##### ✅ Usuarios
##### ✅ Publicaciones
##### ✅ Comentarios
#### Archivos: 15 pts (15%)
##### ✅ Manejo de Archivos
#### General: 21 pts (21%)
##### ✅ Menús
##### ✅ Parámetros
##### ✅ Módulos
##### ✅ PEP8

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Flujo_Principal.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```Funcione.py``` en ```Carpeta Tarea 0```
2. ```parametros.py``` en ```Carpeta Tarea 0```
3. ```comentarios.csv``` en ```Carpeta Tarea 0```
4. ```publicaciones.py``` en ```Carpeta Tarea 0```
5. ```usuarios.py``` en ```Carpeta Tarea 0```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```datetime```: ```now() / datetime```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```Funciones```: Contiene a ```Leer_Archivo()```, ```Verificar_Usuario()```, ```Registrar_Usuario()```, ```Una_Publicacion()```, ```Datos_Publicacion()```, ```Comentarios_Publicacion()```, ```Agregar_Comentario()```, ```Publicaciones_Usuario()```, ```Agregar_Publicaciones()```, ```Eliminar_Publicacion()```, ```Eliminar_Comentario()```, ```Fecha_Emision()```, ```Orden_Fecha()```
2. ```Parametros```: Hecha para <Contener los parametros para poder modificarlos de mejor manera>


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <El nombre de usuario no diferencia entre mayúsculas y minúsculas. Esto lo decidí porque normalmente las aplicaciones que uno utiliza en la actualidad tampoco diferencian, acercando con ello más a la realidad > 
2. <El nombre de usuario no puede ser "anonimo". Esto porque es una palabra clave que utilizo en el codigo para separar a quienes entran en modo anónimo y aquellos que poseen cuenta>
3. <El nombre de usuario tiene que tener un largo mayor a 1 caracter. Dado que al escribir en el archivo de comentarios se genera una linea vacia y de forma que esta linea no sea leida y guardada en las listas que utilizo para imprimir los comentarios, fue necesario tener la condicion de que el largo de la linea sea mayor a un caracte. Aunque no presente este problema en el archivo de usuarios, mantuve la medida de forma preventiva.>
4. <En algunos casos al terminar el programa, saliendo de el a través de las respuestas (opcion 4 en menu inicio) y haber entrado con una cuenta. Este vuelve a entrar en el menu de las publicaciones realizadas, y al volver hacer el camino de salida está se da sin problemas. Esto no ocurre siempre, y no tiene sentido con el código escrito, dado que se inicia y termina a través del menú inicio y este no tiene una relación directa con el otro menú. Por ello creo que es un problema de mi computador. Pero prefiero que quede la situación ecrita por si llega a ocurrir al corregir.>


-------
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://es.acervolima.com/2021/02/09/python-ordenar-lista-de-fechas-dadas-como-cadenas/>: este hace \<Ordena una lista de fechas desde la más antigua a la más nueva> y está implementado en el archivo <Funciones.py> en las líneas <222> y hace <Ordena las fechas y horarios que entregue desde la más antigua a la más nueva utilizando el formato entregado para imprimir las fechas y no el utilizado en internet>



## Descuentos
La guía de descuentos se encuentra (https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
