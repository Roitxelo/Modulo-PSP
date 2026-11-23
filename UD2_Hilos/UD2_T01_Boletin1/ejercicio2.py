import threading

class HiloA(threading.Thread):

    def run(self):
        for i in range(30):
            print("NO")


class HiloB(threading.Thread):

    def run(self):
        for i in range(30):
            print("YES")


if __name__ == "__main__":

    hiloA = HiloA()
    hiloB = HiloB()

    print("Ejecución en HiloA")
    hiloA.start()

    print("\nEjecución en HiloB")
    hiloB.start()

    print("\nEjecución en main")