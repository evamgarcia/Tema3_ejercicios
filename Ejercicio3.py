
class nave():
    def __init__(self, nombre, largo, tripulacion, cantidad_pasajeros):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidad_pasajeros = cantidad_pasajeros
    def __str__(self):
        return "La nave: {}, tiene {} de largo, con una tripulacion de {}, caben pasajeros {}".format(self.nombre, self.largo, self.tripulacion, self.cantidad_pasajeros)

Nave_Estrella = nave("Estresalla_de_la_muerte", 160000, 1281670, 10000)
Nave_Halcon = nave("Halcon_milernario", 34, 5, 3)
Nave_Tie = nave("Caza_Tie", 6, 1, 1) 
Nave_Ala_x = nave("Ala_x", 13, 1, 1)
Nave_Destructor = nave("Destructor_estelar", 1300, 5400, 5400)

lista= [Nave_Destructor, Nave_Ala_x, Nave_Tie, Nave_Estrella, Nave_Halcon]
print(Nave_Estrella, Nave_Destructor)
