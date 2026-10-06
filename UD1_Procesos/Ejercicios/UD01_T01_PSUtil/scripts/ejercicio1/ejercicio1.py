import psutil
import json
from datetime import datetime
from pathlib import Path


def obtener_informacion():

    # PLATAFORMA
    if psutil.WINDOWS:
        plataforma = "Windows"
    elif psutil.LINUX:
        plataforma = "Linux"
    else:
        plataforma = "Otro sistema"


    # CPU
    numero_cpus = psutil.cpu_count()

    frecuencias = psutil.cpu_freq(percpu=True)

    lista_frecuencias = []

    if frecuencias is not None:
        for frecuencia in frecuencias:
            lista_frecuencias.append(frecuencia.current)

    uso_cpu = psutil.cpu_percent(interval=1, percpu=True)


    # MEMORIA
    memoria = psutil.virtual_memory()


    # DISCOS
    lista_particiones = []

    for particion in psutil.disk_partitions():

        try:
            uso = psutil.disk_usage(particion.mountpoint)

            datos_particion = {
                "unidad": particion.device,
                "ruta": particion.mountpoint,
                "sistema_archivos": particion.fstype,
                "total_bytes": uso.total,
                "usado_bytes": uso.used,
                "libre_bytes": uso.free,
                "porcentaje_usado": uso.percent
            }

            lista_particiones.append(datos_particion)

        except (PermissionError, OSError):
            pass


    disco = psutil.disk_io_counters()


    # RED
    red = psutil.net_io_counters()


    # DICCIONARIO CON TODA LA INFORMACIÓN
    informacion = {

        "plataforma": plataforma,

        "cpu": {
            "numero_cpus": numero_cpus,
            "frecuencia_mhz": lista_frecuencias,
            "uso_por_cpu": uso_cpu
        },

        "memoria": {
            "memoria_total": memoria.total,
            "memoria_disponible": memoria.available,
            "porcentaje_usado": memoria.percent
        },

        "discos": {
            "particiones": lista_particiones,
            "operaciones_lectura": disco.read_count,
            "operaciones_escritura": disco.write_count,
            "bytes_leidos": disco.read_bytes,
            "bytes_escritos": disco.write_bytes
        },

        "red": {
            "bytes_enviados": red.bytes_sent,
            "bytes_recibidos": red.bytes_recv,
            "paquetes_enviados": red.packets_sent,
            "paquetes_recibidos": red.packets_recv
        }
    }

    return informacion


def mostrar_informacion():

    informacion = obtener_informacion()

    print("\n-----------------------------")
    print(" INFORMACIÓN DEL SISTEMA")
    print("-----------------------------")

    print(json.dumps(informacion, indent=4, ensure_ascii=False))


def guardar_informacion():

    ruta = input("Introduce la ruta donde guardar el archivo: ")

    carpeta = Path(ruta)

    if not carpeta.is_dir():
        print("La ruta introducida no existe.")
        return

    informacion = obtener_informacion()

    fecha = datetime.now().strftime("%Y%m%d%H%M%S")

    nombre_archivo = fecha + "-system-info.json"

    archivo = carpeta / nombre_archivo

    with open(archivo, "w", encoding="utf-8") as fichero:
        json.dump(informacion, fichero, indent=4, ensure_ascii=False)

    print("Información guardada correctamente.")
    print("Archivo:", archivo)


# MENÚ PRINCIPAL

opcion = 0

while opcion != 3:

    print("\n-----------------------------")
    print(" INFORMACIÓN DEL SISTEMA")
    print("-----------------------------")
    print("1. Mostrar información del sistema")
    print("2. Guardar información del sistema")
    print("3. Salir")

    try:
        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            mostrar_informacion()

        elif opcion == 2:
            guardar_informacion()

        elif opcion == 3:
            print("Programa finalizado.")

        else:
            print("Opción incorrecta.")

    except ValueError:
        print("Debes introducir un número.")