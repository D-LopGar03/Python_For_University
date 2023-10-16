import random, os, time

main_vector = []

def limpiar_pantalla():
    if os.name=="NT":
        os.system("cls")
    else:
        os.system("clear")

def ingresar_Valores_Random(main_vector):
    for i in range(0, 50):
        numero_aleatorio = random.randint(0, 50)
        main_vector.append(numero_aleatorio)
    return len(main_vector)

def buscar_no_repetidos(main_vector):
    no_repetidos = []
    
    for i in main_vector:
        if main_vector.count(i) == 1:
            no_repetidos.append(i)
    
    print("Lista Original:", main_vector)
    print("Valores No Repetidos:", no_repetidos,"\n\n")

    return len(no_repetidos)

def contar_repetidos(main_vector):

    print("{:<10} {:<15}".format("Elemento", "Repeticiones"))
    
    for i in main_vector:
        repeticion = main_vector.count(i)
        # Imprime cada fila de la tabla
        
        print("{:<10} {:<15}".format(i, repeticion, i, repeticion))

def num_teclado(main_vector):

    num = int(input("\n\nIngrese un valor entero entre 1 y 20 para buscar en el arreglo: "))

    if num in main_vector:
        repeticion = main_vector.count(num)

        if repeticion == 1:
            print(f"{num} se repite {repeticion} vez")
        elif repeticion >1:
            print(f"{num} se repite {repeticion} veces")        
    else:
        print(f"{num} no se encuentra dentro del arreglo principal")     

def bienvenida():
    
    limpiar_pantalla()
    # Generar valores aleatorios
    print(f"El primer vector tiene un largo de {ingresar_Valores_Random(main_vector)} posiciones\n\n")
    # Encontrar valores no repetidos
    print(f"El segundo vector tiene un largo de {buscar_no_repetidos(main_vector)} posiciones\n\n")
    time.sleep(6)
    limpiar_pantalla()
    # Encontrar veces repetidos los valores
    contar_repetidos(main_vector)
    # Encontrar y contar cuantas veces se repite un valor buscado por teclado
    num_teclado(main_vector)
    time.sleep(3)
    limpiar_pantalla()



