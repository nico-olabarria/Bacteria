import os
import pandas as pd 

def comprobacion_memoria(name, df):
        # Devolucion de si la bacteria esta registrada o no
        registro = name in set(df['Nombre'])
        return registro

def cambio_elemento(name, df):
        aux_df = df.loc[df.isin([name])]
        print(aux_df)

        return df
def guardado_permanente(rate):
        
        # Comprobacion de la existencia de la libreria
        try:
                # Lectura del .csv
                memory_df = pd.read_csv('memoria\\bacteria_library.csv')
        except OSError:
                ans = input("No existe la biblioteca de bacterias, ¿le gustaría crearla? [y/n]: ")
                
                # Creacion de la libreria de bacterias
                if ans.upper() == "Y":
                        memory_df = pd.DataFrame(columns = ["Nombre", "Ratio de crecimiento"])

        # Nombre de la bacteria a introducir
        nombre = input("Introduzca el nombre de la bacteria: ")

        # Comprobacion de si el nombre existe en la libreria
        registro = comprobacion_memoria(nombre, memory_df)
        # Inclusion de la nueva linea de datos
        if registro == False:
                data_list = [nombre, rate]
                print(data_list)
                length = len(memory_df)
                memory_df.loc[length] = data_list
                print(memory_df)

                # Traspaso a un .csv
                memory_df.to_csv('memoria\\bacteria_library.csv', index = False)
        else:
                memory_df = cambio_elemento(nombre, memory_df)
                


