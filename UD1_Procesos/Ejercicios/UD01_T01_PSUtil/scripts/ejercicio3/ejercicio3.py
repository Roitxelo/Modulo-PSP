import psutil


def mostrar_informacion():



opcion = 0

while opcion != 5:

    print("\n------------------------------")
    print(" MENÚ DE PROCESOS DEL SISTEMA")
    print("------------------------------")
    print("1. Mostrar todos los procesos")
    print("2. Filtrar por uso de memoria")
    print("3. Filtrar por uso de CPU")
    print("4. Mostrar árbol de procesos")
    print("5. Salir")

    try:
        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            mostrar_informacion()

        elif opcion == 2:
            filtrar_por_memoria()

        elif opcion == 3:
            filtrar_por_CPU()

        elif opcion == 4:
            mostrar_arbol()

        elif opcion == 5:
            print("\nGracias por utilizar el menú... Vuelve pronto!")

        else:
            print("\nOpción incorrecta...")

    except ValueError:
        print("Debes introducir un número...")



    def imprimir(p, decoracion="")

    print(f"{decoracion}-{pinombre}-p")

    for phijo in hijos:
        imprimir(phijo, decoracion=decoracion+" ")