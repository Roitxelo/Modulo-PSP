import multiprocessing

def incrementar(contador, lock):
    for i in range(100):
        with lock:
            contador.value += 1

if __name__ == "__main__":
    contador = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    procesos = []

    for i in range(3):
        p = multiprocessing.Process(target=incrementar, args=(contador, lock))
        procesos.append(p)
        p.start()

    for p in procesos:
        p.join()

    print("Contador final:", contador.value)