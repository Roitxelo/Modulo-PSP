import threading

class MiHilo(threading.Thread):

    def run(self):
        for i in range(1000):
            print("NO")


if __name__ == "__main__":

    hilo = MiHilo()
    hilo.start()

    for i in range(1000):
        print("YES")