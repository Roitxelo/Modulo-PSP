import multiprocessing
import random

def agregar_al_diccionario(diccionario, clave):
    diccionario[clave] = random.randint(1,100)


if __name__ == "__main__":

    with multiprocessing.Manager() as manager:

        diccionario = manager.dict
        procesos = []

        for i in range:
          p = multiprocessing.Process(target=agregar_al_diccionario, args=(diccionario, f"clave{i}",))
          procesos.append(p)
          p.start

        for p in procesos:
           p.join()

    