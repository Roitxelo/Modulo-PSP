import psutil

def mostrar_servicio(datos):
    print(f"Nombre: {datos.get('name')}")
    print(f"PID: {datos.get('pid') or 'Sin PID'}")
    print(f"Estado: {datos.get('status')}")
    print(f"Tipo de inicio: {datos.get('start_type')}")
    print("------------------------------------------")

def mostrar_todos():

    for servicio in psutil.win_service_iter():
        datos = servicio.as_dict()
        mostrar_servicio(datos)


def mostrar_filtrados():

    filtro = input(
        "Introduce el filtro (iniciado/parado manual/automático): "
    ).lower().split()

    if len(filtro) < 1 or len(filtro) > 2:
        print("Debes introducir una o dos palabras.")
        return


    estados = {
        "iniciado": "running",
        "parado": "stopped"
    }

    tipos_inicio = {
        "manual": "manual",
        "automático": "automatic",
        "automatico": "automatic"
    }

    if filtro[0] not in estados:
        print("El estado debe ser 'iniciado' o 'parado'.")
        return

    if len(filtro) == 2:
        if filtro[1] not in tipos_inicio:
            print("El tipo de inicio debe ser 'manual' o 'automático'.")
            return

    encontrados = 0

    for servicio in psutil.win_service_iter():

        datos = servicio.as_dict()

        estado_correcto = datos.get("status") == estados[filtro[0]]

        if len(filtro) == 1:
            inicio_correcto = True

        else:
            inicio_correcto = (
                datos.get("start_type") == tipos_inicio[filtro[1]]
            )

        if estado_correcto and inicio_correcto:
            mostrar_servicio(datos)
            encontrados += 1


    print(f"\nServicios encontrados: {encontrados}")


def mostrar_descripcion():

    nombre = input("Introduce el nombre del servicio: ").strip()

    try:
        servicio = psutil.win_service_get(nombre)
        print(f"\nNombre: {nombre}")
        print(f"Descripción: {servicio.description()}")

    except psutil.NoSuchProcess:
        print("No se ha encontrado ese servicio.")

    except Exception:
        print("No se ha podido obtener la información del servicio.")

opcion = ""

while opcion != "4":

    print("\n------------------------------")
    print(" SERVICIOS DE WINDOWS")
    print("------------------------------")
    print("1. Mostrar todos los servicios")
    print("2. Mostrar servicios filtrados")
    print("3. Mostrar descripción de un servicio")
    print("4. Salir")

    opcion = input("\nElige una opción: ")

    if opcion == "1":
        mostrar_todos()
    elif opcion == "2":
        mostrar_filtrados()
    elif opcion == "3":
        mostrar_descripcion()
    elif opcion == "4":
        print("Programa finalizado.")
    else:
        print("Opción no válida.")