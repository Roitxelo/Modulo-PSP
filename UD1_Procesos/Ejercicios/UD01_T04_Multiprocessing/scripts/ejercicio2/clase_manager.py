import multiprocessing
import random
import time

def agregar_al_diccionario(diccionario, id_proceso):
    time.sleep(random.random())

    valor = random.randint(1,100)
    
    diccionario[clave] = valor

    print(f"Proceso {id_proceso} añadio: {clave} = {valor}")

if __name__ == "__main__":

    with multiprocessing.Manager() as manager:

        diccionario = manager.dict
        procesos = []
        cantidad_procesos = [4]

        for i in range(cantidad_procesos):
          p = multiprocessing.Process(target=agregar_al_diccionario, args=(diccionario, f"clave{i}",))
          procesos.append(p)
          p.start
          p.join

    print(diccionario)