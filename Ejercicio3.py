
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

lista_naves = [Nave_Destructor, Nave_Ala_x, Nave_Tie, Nave_Estrella, Nave_Halcon]
print(Nave_Estrella, Nave_Destructor)

lista_ordenada_pasajeros = sorted(lista_naves, key=lambda x: x.cantidad_pasajeros, reverse=True)
lista_ordenada_tripulacion = sorted(lista_naves, key=lambda x: x.tripulacion, reverse=True)
lista_ordenada_largo = sorted(lista_naves, key=lambda x: x.largo)

def mostrar_cinco_naves_mas_pasajeros (e):
    print("Estas son las cinco naves con mas pasajeros: ")
    for i in range(5):
        if i < len(e):
            print(e[i])

def mostrar_naves_mas_tripulacion(e):
    print("Esta es la nave con mas tripulacion: ", e[0])

def mostrar_naves_mayor_menor_tamaño(e):
    print("Esta es la nave con mas tamaño: ", e[len(e)-1], "nave con menos tamaño: ", e[0])

mostrar_cinco_naves_mas_pasajeros(lista_ordenada_pasajeros)
mostrar_naves_mas_tripulacion(lista_ordenada_tripulacion)
mostrar_naves_mayor_menor_tamaño(lista_ordenada_largo)

def mostrar_mas_seis_pasajeros(e):
    for i in e:
        if i.cantidad_pasajeros >= 6:
            print(i)
mostrar_cinco_naves_mas_pasajeros(lista_naves)
mostrar_naves_mas_tripulacion(lista_naves)
mostrar_naves_mayor_menor_tamaño(lista_naves)