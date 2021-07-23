from math import e
import matplotlib.pyplot as plt
import pandas as pd
import random
from decimal import Decimal
import memoria

def bacteria_growth_formula(Pop_ini, time, growth_rate):
    Pop = Pop_ini * float(e) ** (growth_rate * time)

    return Pop

x = []
y = []

# Numero de colonias
n = random.randint(1, 10)

print('Habrá ' + str(n) + ' colonias')

# Localizacion de las colonias
for i in range(0, n):
    x.append(random.randint(0, 20))
    y.append(random.randint(0, 20))

# Generacion de la cantidad de bacterias

time = input("Introduzca en segundos la duración del cultivo: ")
time_list = []

for i in range(0, int(time)):
    time_list.append(i)


rate = input("Introduzca el ratio de crecimiento: ")

memoria.guardado_permanente(rate)

# Ploteo
#plt.figure("Random points")

#for i in range(0, len(x)):
#    plt.scatter(x[i], y[i], size[i])

#plt.show()
