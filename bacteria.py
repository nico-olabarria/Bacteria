# Este archivo servirá como referencia para crear/manejar clases en python
from matplotlib import animation
import numpy as np
import pandas as pd
from math import e
from math import pi
from math import sqrt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


class bacteria():
    def __init__(self, bac_name, col_name, growth_rate=1, x=0, y=0, ini_pop=1, colour='yellow'):
        # Cada colonia de bacterias tendrá el nombre de la especie, el nombre de la colonia, la velocidad de
        # propagación, coordenadas iniciales de colonia y color asociado a la colonia. Por defecto la velocidad de
        # propagación será igual a 1, el color será amarillo y se encontrará en el origen.
        self.bac_name = bac_name
        self.col_name = col_name
        self.growth_rate = growth_rate
        self.x = x
        self.y = y
        self.ini_pop = ini_pop
        self.colour = colour

    def change_col_name(self, new_name):
        # Función para cambiar el nombre de la bacteria
        self.col_name = new_name

    def change_gr(self, new_growth):
        # Función para cambiar la velocidad de crecimiento de la bacteria
        self.growth_rate = new_growth

    def change_colour(self, new_colour):
        # Función para cambiar el color de la colonia
        self.colour = new_colour


def bacteria_growth_formula(pop_ini, time, growth_rate):
    pop = pop_ini * float(e) ** (growth_rate * time)
    return pop

def plot_colony_growth():
    # Esta función simple plotea una colonia de bacterias en coordenadas (0,0) con una velocidad de crecimiento de 1
    figure, axes = plt.subplots()
    axes.set_aspect(1)
    time = input("Introduzca en segundos la duración del cultivo: ")

    for i in range(0, int(time)):
        area = bacteria_growth_formula(1, time=i, growth_rate=1)
        rad = sqrt(area / pi)
        draw_circle = plt.Circle((0, 0), rad, color='red', alpha=0.2)
        axes.add_artist(draw_circle)
        plt.title('Bacteria')

    plt.show()

def plot_colony_scatter(coords_x, coords_y, growth_rate, time):
    # Muestra el crecimiento de distintas colonias en coordenadas aleatorias a lo largo del tiempo.
    figure = plt.figure()
    axes = plt.axes()

    sizes_in_time = np.zeros(len(coords_x), dtype = [('size', 'float')])

    scatter = plt.scatter(coords_x, coords_y, sizes_in_time)

    
    
    def growth_function(frame_number):
        sizes_in_time['size'] = bacteria_growth_formula(1, time, growth_rate)
        return sizes_in_time
    
    anim = animation.FuncAnimation(figure, growth_function, interval = time)

    plt.show()