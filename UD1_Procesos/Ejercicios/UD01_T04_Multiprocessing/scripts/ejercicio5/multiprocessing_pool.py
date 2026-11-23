import multiprocessing

def cuadrado(numero):
    return numero ** 2

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]

    with multiprocessing.Pool(processes=3) as pool:
        resultados = pool.map(cuadrado, numeros)

    print("Resultados:", resultados)

    