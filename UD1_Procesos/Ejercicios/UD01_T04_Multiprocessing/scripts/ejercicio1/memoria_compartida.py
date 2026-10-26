import multiprocessing


def llenar_lista(lista):
    print("Llenando lista: ")

    for i in range(10): 
        lista[i] = i + 1

def multiplicar_por_dos(lista):
    print("Multiplicando x2")

    for i in range(10):
        lista[i] *=2

if __name__ == "__main__":  

    lista = multiprocessing.Array("i", 10)
    
    # creating processes
    p1 = multiprocessing.Process(target=llenar_lista, args=(lista, ))
    p2 = multiprocessing.Process(target=multiplicar_por_dos, args=(lista, ))

    # starting process 1
    p1.start()
    # starting process 2
    p2.start()

    # wait until process 1 is finished
    p1.join()
    # wait until process 2 is finished
    p2.join()

    # both processes finished
    print(list(lista))
