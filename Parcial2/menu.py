from random_Vector import bienvenida, limpiar_pantalla
from matrix import main
import time

limpiar_pantalla()



if __name__ == "__main__":
    try:
        while True:

            choice  = int(input("SELCCIONA UNA OPCIÓN: \n\n1) Vectores\n\n2) Matrices\n\n3)Salir\n\nTu respuesta ==>> "))

            if choice == 1:

                bienvenida()
            elif choice == 2:
                
                main()
            elif choice == 3:
                print("Ok")
                time.sleep(1.5)
                limpiar_pantalla()
                break
            else:
                print("Opción no encontrada")
                time.sleep(2)
                limpiar_pantalla()
    except KeyboardInterrupt:
        limpiar_pantalla()