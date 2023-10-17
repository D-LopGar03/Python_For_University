import random
import numpy as np
from random_Vector import limpiar_pantalla

# Función para imprimir una matriz (La usaremos para imprimir matrices sin encesidad de reescribir el print)
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para imprimir un vector (La usaremos despues)
def imprimir_vector(vector):
    print(vector)

def main():

    limpiar_pantalla()

    # Generar la matriz 5x5 con números aleatorios en el rango de 100 a 200
    matriz_uno = [[random.randint(100, 200) for i in range(5)] for j in range(5)]

    # Imprimir la matriz uno
    print("Matriz Uno:")
    imprimir_matriz(matriz_uno)

    # Inicializar la matriz dos como una copia de la matriz uno
    matriz_dos = [fila.copy() for fila in matriz_uno]

    # Aplicar operaciones a la matriz dos según las instrucciones dadas
    for fila in range(5):
        # Elevar al cuadrado los valores de la primera columna
        matriz_dos[fila][0] = matriz_uno[0][fila] ** 2
        # Elevar a la cuarta los valores de la segunda columna
        matriz_dos[fila][1] = matriz_uno[1][fila] ** 4

    # Imprimir la matriz dos después de aplicar las operaciones
    print("\nMatriz Dos:")
    imprimir_matriz(matriz_dos)

    # Sumar cada una de las filas de la matriz uno y almacenar los resultados en un vector
    vector_suma_filas_uno = [sum(fila) for fila in matriz_uno]
    print("\nVector Suma Filas Matriz Uno:")
    imprimir_vector(vector_suma_filas_uno)

    # Sumar cada una de las columnas de la matriz dos y almacenar los resultados en un vector
    vector_suma_columnas_dos = [sum(fila) for fila in zip(*matriz_dos)]
    print("\nVector Suma Columnas Matriz Dos:")
    imprimir_vector(vector_suma_columnas_dos)

    # Calcular la matriz diferencia de Matriz dos menos matriz uno
    matriz_diferencia = np.subtract(matriz_dos, matriz_uno)
    print("\nMatriz Diferencia (Matriz Dos - Matriz Uno):")
    imprimir_matriz(matriz_diferencia)

    # Calcular el producto de una matriz por un número (El numero que se va a usar es 2)
    escalar = 2
    matriz_producto_numero = np.multiply(matriz_uno, escalar)
    print("\nMatriz Producto por Número:")
    imprimir_matriz(matriz_producto_numero)

    # Generar otra matriz 5x5 con números aleatorios para multiplicar con la matriz uno
    matriz_multiplicacion = [[random.randint(1, 5) for i in range(5)] for j in range(5)]

    # Calcular el producto de 2 matrices
    matriz_producto = np.dot(matriz_uno, matriz_multiplicacion)
    print("\nMatriz Producto (Matriz Uno x Matriz Multiplicacion):")
    imprimir_matriz(matriz_producto)

    # Sumar la diagonal principal de la matriz uno
    suma_diagonal_uno = np.trace(matriz_uno)
    print("\nSuma Diagonal Principal Matriz Uno:", suma_diagonal_uno)

    # Sumar la diagonal inversa de la matriz dos
    suma_diagonal_inversa_dos = np.trace(np.linalg.inv(matriz_dos))
    print("Suma Diagonal Inversa Matriz Dos:", suma_diagonal_inversa_dos)

    # Calcular la media de todos los elementos de la matriz producto
    media_matriz_producto = np.mean(matriz_producto)
    print("Media de la Matriz Producto:", media_matriz_producto)