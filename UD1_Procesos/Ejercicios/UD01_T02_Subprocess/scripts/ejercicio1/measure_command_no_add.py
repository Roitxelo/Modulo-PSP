# python measure_command.py ping as.com
# salida esperada: 

# Ejecutando: ping as.com
# Salida del proceso:
# Tarea terminada
# Tiempo de ejecución: 2.01 segundos
# Código de salida 0


import sys
import subprocess
import time


argumentos = sys.argv[1:]

inicio = time.perf_counter()
resultado = subprocess.run(argumentos, capture_output=True, text=True, shell=True)
fin = time.perf_counter()

print(f"""
Ejecutando: {" ".join(argumentos)}
Salida del proceso: 
{resultado.stdout} 
{resultado.stderr}
Tarea terminada
Tiempo de ejecución: {(fin-inicio):2.2f} segundos
Código de salida: {resultado.returncode}
""")