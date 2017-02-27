"""
# PROYECTO #1
# Laboratorio de Algoritmos y Estructuras II (CI2692)
# Descripcion: Modulo con la implementacion de algoritmos de ordenamientos
#              que son aplicados sobre listas de elementos de tipo numerico
# Autores:  Mario Quintero (13-11148)
#           Carolina Rivas (13-11209)
"""

"""
¡¡¡FALTA POR COMENTAR!!!

"""

from arrayT import ArrayT
import random, math, sys

sys.setrecursionlimit(10000000)

def swap(array,i,j):
    """
    Define el intercambio de dos elementos en un arreglo
       
    Parametros:
        array: Arreglo del que se intercambiaran los elementos
        i,j: Indices de los elementos a intercambiar
    """
    array[i],array[j] = array[j],array[i]

def insertion_sort(array):
    """Ordenamiento por medio del algoritmo de insercion (con solo un argumento)
    Basado en el libro de Kaldewaij

    Parametros:
        array: arreglo a ordenar
    """
    p = 0
    r = len(array)
    for j in range(p+1,r):
        key = array[j]
        i = j - 1
        while i >= p and array[i] > key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key

def insertion_sort2(array, p, r):
    #    """
    #    Ordenamiento por medio del algoritmo de Insertion
    #
    #    Parametros:
    #        array: Un arreglo a ordenar
    #
    #    Efecto Secundario:
    #        El arreglo de entrada es ordenado en orden ascendente
    #    """
    for j in range (p + 1,r):
        key = array[j]
        i = j - 1
        while i >= p and array[i] > key :
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key


def bubble_sort(array):
    """
    Ordenamiento por medio del algoritmo de Bubble Sort
    Basado en el libro de Kaldewaij

    Parametros:
        array: Arreglo a ordenar
    """
    i = 0
    while (i != len(array)):
        j = len(array) - 1
        while j != i:
            if array[j-1] > array[j]:
                swap(array,j,j-1)
            j -= 1
        i += 1

def selection_sort(array):
    """
    Ordenamiento por medio del algoritmo de Selection Sort
    
    Parametros:
        array: Un arreglo a ordenar
    
    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente
    """
    for i in range (0 , len(array)-1):
        for j in range (i + 1, len(array)):
            if array[i] > array[j]:
                swap(array,i,j)

def bubble_sort_modificado(a):
    """
    Implementacion del algoritmo Bubble Sort (1) del libro 
    Programming: the derivation of algorithms de Kaldewaij.
    
    Parametros:
        a: Un arreglo a ordenar

    Efecto Secundario:
        El arreglo de entrada es ordenado en orden ascendente
    """
    N = len(a)
    n = 0
    b = False
    while (n != N) and (not b):
        k = N - 1
        b = True
        while k != n:
            if a[k-1] > a[k]:
                b = False
                swap(a,k,k-1)
            k -= 1
        n += 1

def mergesort(array):
    """
    Implementacion del algoritmo Mergesort del Kaldewaij.

    Parametro:
        array: Arreglo a ordenar

    Efecto Secundario:
        El arreglo se ordena ascendente
    """
    k = 1
    while k < len(array):
        a = 0
        b = k
        c = min(2*k,len(array))
        while b < len(array):
            p = a
            q = b
            r = a
            z = ArrayT(c-a)
            while p != b and q != c:
                if array[p] <= array[q]:
                    z[r-a] = array[p]
                    r = r + 1
                    p = p + 1
                elif array[q] <= array[p]:
                    z[r-a] = array[q]
                    r = r + 1
                    q = q + 1
            while p != b:
                z[r-a] = array[p]
                r = r + 1
                p = p + 1
            while q != c:
                z[r-a] = array[q]
                r = r + 1
                q = q + 1
            r = a
            while r != c:
                array[r] = z[r-a]
                r = r + 1
            a = a + 2*k 
            b = b + 2*k
            c = min((c+2*k),len(array))
        k = 2*k

def heapify(array, i, length):
    """
    Algoritmo que mantiene la propiedad de heap tipo max.

    Parametros:
        i: Nodo del heap
        array: Arreglo con el que se construye el heap
        length: Tamano del heap
    """
    hijo_izquierdo = left(i)
    hijo_derecho = right(i)

    el_mayor = i

    if hijo_izquierdo < length and array[hijo_izquierdo] > array[i]:
        el_mayor = hijo_izquierdo

    if hijo_derecho < length and array[hijo_derecho] > array[el_mayor]:
        el_mayor = hijo_derecho

    if el_mayor != i:
        swap(array,i,el_mayor)
        heapify(array,el_mayor,length)


def build_max_heap(array):
    """
    Crea un heap binario a partir de un arreglo de manera iterativa desde las hojas hasta la raiz.

    Parametros:
        array: Arreglo con el que se construye el heap
    """
    i = (len(array)//2)
    
    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, i, len(array))


def heap_sort(array):
    """
    Ordenamiento por medio del algoritmo de Heapsort.
    Construye un heap con los elementos del arreglo con Buildmaxheap
    e intercambia las posiciones finales con las iniciales, hasta vaciarse el heap.

    Parametros>
        array: Arreglo a ordenar
    """
    i = (len(array)-1)
    build_max_heap(array)
    
    for i in range(len(array)-1, 0, -1):
        swap(array,0,i)
        heapify(array, 0, i)


def parent(i):
    """
    Formula del padre en un heap.

    Parametros:
        i: Nodo
    """
    return (((i + 1) // 2)-1)

def left(i):
    """
    Formula del hijo izquierdo en un heap.

    Parametros:
        i: Nodo
    """
    return (2*(i+1)-1)

def right(i):
    """
    Formula del hijo derecho en un heap.

    Parametros:
        i: Nodo
    """
    return (2*(i+1))

def Quicksort(array, p, r):
    """
    Ordenamiento por medio del algoritmo de Quicksort.

    Parametros:
        array: Arreglo a ordenar
        p: Posicion inicial.
        r: Posicion final
    """
    if p < r:
        q = Partition(array, p, r)
        Quicksort(array, p, q-1)
        Quicksort(array, q+1, r)

def Partition(array, p, r):
    """
    Rutina clave que retorna un indice y particiona el arreglo en dos subarreglos.
    Se elige un pivote x que en este caso es el ultimo elemento del arreglo.

    Parametros:
        array: Arreglo a ordenar
        p: Posicion inicial
        r: Posicion final
    """
    x = array[r] 
    i = p-1
    for j in range (p,r):
        if array[j] <= x:
            i = i + 1
            swap(array,i,j)
    swap(array,i+1,r)
    return i+1

def quicksort_basico(array):
    """
    Con un solo parametro, esta funcion llama al algoritmo Quicksort estableciendo los otros dos argumentos

    Parametros:
        array: Arreglo a ordenar
    """
    p = 0
    r = len(array)-1
    Quicksort(array,p,r)

def Randomized_partition(array, p, r):
    """
    Cumple la misma funcion que Partition() pero tomando un pivote aleatorio entre el inicio y el final del arreglo

    Parametros:
        array: Arreglo a ordenar
        p: Posicion inicial
        r: Posicion final
    """
    i = random.randint(p,r)
    swap(array,r,i)
    return Partition(array,p,r)

def Randomized_quicksort(array,p,r):
    """
    Ordenamiento por medio del Quicksort randomizado. Utiliza Randomized_partition().

    Parametros:
        array: Arreglo a ordenar
        p: Posicion inicial
        r: Posicion final
    """
    if p<r:
        q = Randomized_partition(array,p,r)
        Randomized_quicksort(array,p,q-1)
        Randomized_quicksort(array,q+1,r)

def quicksort_randomizado(array):
    """
    Con un solo parametro, y luego estableciendo los otros dos argumentos, hace llamada al Quicksort randomizado.

    Parametros:
        array: Arreglo a ordenar
    """
    p = 0
    r = len(array)-1
    Randomized_quicksort(array,p,r)

def Partition_New(array,p,r,x):
    """
    Metodo de particion propuesto por Hoare, que realiza otra division del arreglo.

    Parametros:
        array: Arreglo a ordenar
        p: Inicio
        r: Fin
        x: Pivote
    """
    i = p-1
    j = r
    while True:
        while True:
            j = j - 1
            if array[j] <= x:
                break
        while True:
            i = i + 1
            if array[i] >= x:
                break
        if i < j:
            swap(array,i,j)
        else:
            return j

def median_of_3(a,b,c):
    """
    Retorna la media de tres numeros dados.

    Parametros:
        a,b,c: Tres numeros (enteros o reales)
    """
    if a > b:
        if a < c:
            return a
        elif b > c:
            return b
        else:
            return c

    else:
        if a > c:
            return a
        elif b < c:
            return b
        else:
            return c

def Quicksort_loop(array, p, r):
    """
    Parametros:
        array: Arreglo a ordenar
        p: Inicio del arreglo
        r: Fin del arreglo
    """
    while (r-p)>10:
        l = Partition_New(array,p,r,median_of_3(array[0],array[len(array)//2],array[len(array)-1]))
        if (l - p)>=(r - l):
            Quicksort_loop(array, l, r)
            r = l
            return r
        else:
            Quicksort_loop(array, p, l)
            p = l
            return p

def Quicksort_median_of_3_3ar(array,p,r):
    """
    Llama la funcion Quicksort_loop, y luego se ordena por insercion el arreglo
    Basado en la implementacion de la HP C++ Standard Template Library
    
    Parametros:
        array: Arreglo a ordenar
        p: Inicio del arreglo
        r: Fin del arreglo
    """
    Quicksort_loop(array,p,r)
    insertion_sort(array)

def Quicksort_median_of_3(array):
    """
    Con un parametro y luego estableciendo los otros dos, hace llamada al Quicksort Median of 3 con 3 parametros

    Parametros:
        array: Arreglo a ordenar
    """
    p = 0
    r = len(array)-1
    Quicksort_median_of_3_3ar(array,p,r)

def introsort(array):
    """
    Establece otras dos variables aparte del arreglo, y llama a introsort con tres parametros

    Parametros:
        array: Arreglo a ordenar
    """
    p = 0
    r = len(array)-1
    introsort2(array,p,r)

def introsort2(array,p,r):
    """
    Ordenamiento por medio del algoritmo de Introsort.
    Hace llamada al Introsort Loop.
    Basado en el pseudocodigo de Musser, D.R.

    Parametros:
        array: Arreglo a ordenar
        p: Inicio del arreglo
        r: Fin del arreglo
    """
    k = r - p
    limprof = int(math.floor(math.log(k)))*2
    introsort_loop(array,p,r,limprof)
    insertion_sort(array)

def introsort_loop(array, p, r, depth_limit):
    """
    Dependiendo de la profundidad de la recursion, cambia a heapsort para ordenar el algoritmo
    
    Parametros:
        array: Arreglo a ordenar
        p: Inicio del arreglo
        r: Final del arreglo
        depth_limit: Limite de la profundidad de la recursion
    """
    size_threshold = 10
    while r - p > size_threshold:
        if depth_limit == 0:
            heap_sort(array)
            return
        depth_limit = depth_limit - 1
        l = Partition_New(array,p,r,median_of_3(array[0],array[len(array)//2],array[len(array)-1]))
        introsort_loop(array,l,r,depth_limit)
        r = l


def quicksort_three_way_partition2(array,l,r):
    """
    Ordenamiento por medio del algoritmo de Quicksort Three Way Partition
    Tomado del Sedgewick y Bentley.
    Usa el metodo de particionamiento propuesto por Bentley y McIlroy

    Parametros:
        array: Arreglo a ordenar
        l: Inicio del arreglo
        r: Final del arreglo
    """
    i=l-1
    j=r
    p=l-1
    q=r
    if r <= l:
        return
    pivot=array[r]
    while True:
        i+=1    
        while array[i]<pivot:
            i += 1
        j-=1
        while array[j]>pivot:
            if j==l:
                break
            j -= 1
        if i >= j:
            break
        swap(array,i,j)
        if array[i] == pivot:
            p += 1
            swap(array,p,i)
        if array[j] == pivot:
            q -= 1
            swap(array,j,q)
    swap(array,i,r)
    j = i - 1
    for k in range(l,p):
        swap(array,k,j)
        j -= 1
    i+=1
    for k in range(r-1,q,-1):
        swap(array,i,k)
        i += 1
    quicksort_three_way_partition2(array,l,j)
    quicksort_three_way_partition2(array,i,r)

def quicksort_three_way_partition(array):
    """
    Con un solo argumento (del arreglo), establece otros dos y hace llamada al quicksort 3 way p

    Parametros:
        array: Arreglo a ordenar
    """
    l = 0
    r = (len(array)-1)
    quicksort_three_way_partition2(array,l,r)

def dual_pivot_quicksort3ar(array,left,right):
    """
    Ordenamiento por medio del algoritmo de Dual Pivot Quicksort.
    Su metodo de particionamiento hace que el algoritmo tenga en promedio menos comparaciones.
    Basado en el pseudocodigo de Wild, Nebel, Neininger

    Parametros:
        array: Arreglo a ordenar
        left: Inicio del arreglo
        right: Final del arreglo
    """
    size_threshold = 10
    if right - left <= size_threshold:
        insertion_sort2(array,left,right+1)
    else:
        if array[left] > array[right]:
            p = array[right]
            q = array[left]
        else:
            p = array[left]
            q = array[right]
        l = left + 1
        g = right - 1
        k = l
        while k <= g:
            if array[k] < p:
                swap(array,k,l)
                l = l + 1
            elif array[k] >= q:
                while array[g] > q and k < g:
                    g = g - 1
                if array[g] >= p:
                    swap(array,k,g)
                else:
                    swap(array,k,g)
                    swap(array,k,l)
                    l = l+1
                g = g-1
            k = k + 1
        l = l -1
        g = g +1
        array[left] = array[l]
        array[l] = p
        array[right] = array[g]
        array[g] = q
        dual_pivot_quicksort3ar(array,left, l - 1)
        dual_pivot_quicksort3ar(array, l + 1, g - 1)
        dual_pivot_quicksort3ar(array, g + 1,right)

def dual_pivot_quicksort(array):
    """
    Llama al dual pivot con tres parametros

    Parametros:
        array: Arreglo a ordenar
    """
    left = 0
    right = len(array)-1
    dual_pivot_quicksort3ar(array,left,right)