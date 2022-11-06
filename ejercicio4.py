class Nodo(object):
    info, sig = None, None

class datoPolinomio(object):
    def __init__(self, termino, valor):
        self.valor = valor 
        self.termino = termino 

class Polinomio(datoPolinomio):

    def __init__(self):
        self.termino_mayor = None
        self.grado = -1

    def agregar_termino(self, valor, termino):
        aux = Nodo()
        dato = datoPolinomio(valor, termino)
        aux.info = dato
        if termino > self.grado:
            aux.sig = self.termino_mayor
            self.termino_mayor = aux 
            self.grado = termino 
        else:
            actual = self.termino_mayor
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux

    def modificar_termino(polinomio, termino,valor):
        aux = polinomio.termino_mayor
        while(aux is not None and aux.info.termino != termino):
            aux = aux.sig
        aux.info.valor = valor 

        
    def eliminar_termino(self, termino):
        aux = self.termino_mayor
        if (self.grado == termino):
            self.termino_mayor = aux.sig
            del aux
        else:
            while aux.sig is not None:
                if aux.sig.info.termino == termino:
                    aux.sig = aux.sig.sig
                    del aux.sig
                    return
                aux = aux.sig

    def obtener_valor(self, termino):
        aux = self.termino_mayor
        while (aux is not None and aux.info.termino > termino):
            aux = aux.sig
        if (aux is not None and aux.info.termino == termino):
            return aux.info.valor
        else:
            return o 

    def restar(polinomio1, polinomio2):
        paux = Polinomio()
        mayor = polinomio1 if (polinomio1.grado > polinomio2.grado) else polinomio2
        for i in range(0, mayor.grado-1):
            total = obtener_valor(polinomio1, i) - obtener_valor(polinomio2, i)
            if (total != 0):
                agregar_termino(paux, i, total)
        return paux
            
    def division(polinomio1, polinomio2):
        paux = polinomio1.termino_mayor
        pol1 = polinomio1.termino_mayor
        while(pol1 is not None):
            pol2 = polinomio2.termino_mayor
            while(pol2 is not None):
                termino = pol1.info.termino - pol2.info.termino
                valor = pol1.info.valor / pol2.info.valor
                if (obtener_valor(paux, termino) != 0):
                    valor -= obtener_valor(paux, termino)
                    modificar_termino(paux, termino, valor)
                else:
                    agregar_termino(paux, termino, valor)
                pol2 = pol2.sig
            pol1 = pol1.sig
        return paux
