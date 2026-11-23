import threading

class MiHilo(threading.Thread):

    def __init__(self, inicio, fin, nombre):
        super().__init__()
        self.inicio = inicio
        self.fin = fin
        self.nombre = nombre

    def run(self):
        print(self.nombre, "comienza")

        for i in range(self.inicio, self.fin + 1):
            print(self.nombre, ":", i)

        print(self.nombre, "terminó")


if __name__ == "__main__":

    hiloA = MiHilo(1, 10, "ThreadA")
    hiloB = MiHilo(20, 30, "ThreadB")

    print("Iniciando los threads...")

    hiloA.start()
    hiloB.start()

    print("El programa principal ha terminado")