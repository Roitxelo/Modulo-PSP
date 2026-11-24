import threading
import time
import random

class MiHilo(threading.Thread):

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.tiempo = random.randint(0, 10000)

    def run(self):
        print(f"{self.nombre} va a estar dormido durante {self.tiempo} ms")

        try:
            time.sleep(self.tiempo / 1000)
        except Exception:
            print("Error en el hilo")

        print(f"{self.nombre} ha despertado")


if __name__ == "__main__":

    hilo1 = MiHilo("Hilo1")
    hilo2 = MiHilo("Hilo2")
    hilo3 = MiHilo("Hilo3")

    hilo1.start()
    hilo2.start()
    hilo3.start()