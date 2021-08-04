# Este archivo servirá como referencia para crear/manejar clases en python

class bacteria() :
    def __init__(self, bac_name, col_name, growth_rate=1, x=0, y=0, colour='yellow'):
        # Cada colonia de bacterias tendrá el nombre de la especie, el nombre de la colonia, una velocidad de
        # propagación, coordenadas iniciales de colonia y color asociado a la colonia. Por defecto la velocidad de
        # propagación será igual a 1, el color será amarillo y se encontrará en el origen.
        self.bac_name = bac_name
        self.col_name = col_name
        self.growth_rate = growth_rate
        self.x = x
        self.y = y
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


