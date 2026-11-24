import threading
import time

class MiHilo(threading.Thread):

    def run(self):
        for i in range(1, 101):
            time.sleep(0.1)
            print(f"ID: {self.ident} - Nombre: {self.name} - Número: {i}")


if __name__ == "__main__":

    inicio = time.time()

    hilo = MiHilo()
    hilo.start()

    hilo.join()

    fin = time.time()

    print(f"Tiempo final de ejecución: {fin - inicio} segundos")