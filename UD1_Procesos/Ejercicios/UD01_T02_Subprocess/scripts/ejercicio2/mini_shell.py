import sys
import subprocess

argumentos = sys.argv[1:]

resultado = subprocess.run(argumentos, capture_output=True, text=True, shell=True)

print(f"""MiniShell
      Escribe 'exit' para terminar
      >  """)


nombre_fichero_alias = "aliases.txt"
alias = {}

with open(nombre_fichero_alias) as fichero:
    
#     # separar linea en dos partes
#     for linea in fichero.readlines():
#             k,v = linea.strip("\n").split("=")
#             alias[k] = v

      # Alternativa en una linea
      alias = { k:v for k,v in list(map(lambda linea: linea.strip("\n").split("=") , fichero.readlines()))}

print(alias)

    #meter cosas en el diccionario alias