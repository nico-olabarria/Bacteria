import pandas as pd

def tareas():
        options = pd.Series(range(0, 3))
        print("0. Registrar bacteria\n 1. Plotear bacteria \n 2. Salir")
        while True:
                ans = input("¿Qué desea hacer?: ")
                if options.isin(ans) == True:
                        break
                else:

        