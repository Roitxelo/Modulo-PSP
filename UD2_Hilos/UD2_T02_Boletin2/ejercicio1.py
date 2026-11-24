import threading
import time

class MiHilo(threading.Thread):

    def run(self):
        try:
            time.sleep(2)
        except Exception:
            print("Error")

if __name__ == "__main__":

    hilo = MiHilo()

    print("Antes de iniciar:", hilo.is_alive())

    hilo.start()
    print("Durante la ejecución:", hilo.is_alive())

    hilo.join()
    print("Después de terminar:", hilo.is_alive())