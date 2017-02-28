#Estudio experimental de algoritmos de ordenamientos sobre diferentes conjuntos de datos

##Los algoritmos utilizados fueron los siguientes:

1. Mergesort
2. Heapsort
3. Quicksort aleatorio
4. Median-of-3 quicksort
5. Introsort
6. Quicksort with 3-way partitioning
7. Dual pivot Quicksort

##El proyecto posee los siguientes archivos:

*- arrayT.py *:
	
	Archivo proporcionado por los profesores de laboratorio.
	El mismo se encarga de implementar el Tipo Abstracto de Datos (ADT) o Clase Arreglo de T con ayuda del modulo 
	<ctypes> de pyhton.

*- ordenamiento.py*:
	
	Archivo o módulo con la implementacion de algoritmos de ordenamientos antes citados. Estos algoritmos son 
	aplicados sobre listas de elementos de tipo numerico 

*- cliente_ordenamiento.py*:

	Cliente o main del proyecto. Importa los algoritmos de ordenamiento para realizar una comparar el desempeño entre
	ellos a traves del tiempo y graficas. Funciona creando arreglos de distintos tamaños con números aleatorios.

	###A continuacion se enumeran la lista de pruebas p sobre las que se medira el desempeno de cada algoritmo:

		1. Enteros aleatorios: Genera un arreglo con números enteros aleatorios comprendidos en el intervalo [0, 500] 

		2. Orden inverso: Genera un arreglo de tamaño N en orden inverso.

		3. Cero-uno: Ceros y unos generados aleatoriamente.

		4. Ordenado: Si el tamaño del arreglo es N , entonces el arreglo contendrá la secuencia
			1, 2, . . . , N − 1, N .

		5. Reales aleatorios: Números reales comprendidos en el intervalo [0, 1) generados
			aleatoriamente.

		6. Mitad: Dado un arreglo de tamaño N , el arreglo contiene como elementos la secuen-
		cia de la forma 1, 2, . . . , N/2, N/2, . . . , 2, 1.

		7. Casi ordenado: Dado un conjunto ordenado de N elementos de tipo entero, se es-
		cogen al azar n/4 pares de elementos que se encuentran separados 4 lugares, entonces
		se intercambian los pares.



##El proyecto puede probarse de la siguiente manera:

	La aplicación cliente ordenamiento.py se ejecuta con la siguiente llamada:
	>./cliente_ordenamiento.py [-h] [-g] [n_elems [n_elems ...]] [-p n_prueba] [-t NT] 
	donde:
	-h: Muestra la ayuda para ejecutar la aplicación.
	-g: Muestra una gráfica con los resultados. Por defecto no se muestra la gráfica.
	-p n_prueba: Selecciona una de las pruebas mencionadas anteriormente, para probar los algoritmos.
				n_prueba representa la prueba a la que se desea someter todos los algoritmos
	-t NT : Ejecuta cada uno de los algoritmos NT veces, para cada arreglo de datos.
			Por defecto NT = 1.
			[n_elems [n_elems ...]] : Lista con los números de elementos de los arreglos a
			ordenar. Si no se indica ninguna lista, por defecto se ordenará un arreglo con 200
			elementos.

####Por ejemplo, una llamada válida en donde se ejecutarı́a la aplicación es:

>./cliente_ordenamiento.py -g 100 200 300 400 -p 3 -t 3

####El proyecto fue implementado utilizando python3