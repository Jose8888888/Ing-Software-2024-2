import sys


def numValles(cadena):
    altura = 0
    valles = 0

    for letra in cadena:
        if letra == 'U':
            altura += 1
            if altura == 0:
                valles +=1
        elif letra == 'D':
            altura -= 1
        else:
            print("La entrada debe ser una cadena que contenga solo las letras U y D")
            sys.exit()

    return valles


class Nodo:
        izquierdo = None
        derecho = None
        padre = None
        elemento = 0

        def __init__(self, elemento: int):
            self.elemento = elemento

        def agrega(self, elemento):
            if elemento <= self.elemento:
                if not (self.izquierdo is None):
                    self.izquierdo.agrega(elemento)
                else:
                    self.izquierdo = Nodo(elemento)
                    self.izquierdo.padre = self
            else:
                if not (self.derecho is None):
                    self.derecho.agrega(elemento)
                else:
                    self.derecho = Nodo(elemento)
                    self.derecho.padre = self

        



class Arbol:
    raiz = None 

    def __init__(self, elemento: int):
            self.raiz = Nodo(elemento)

    def agrega(self, elemento):
        self.raiz.agrega(elemento)

    def preOrden(self):
        l = list()
        l.append(self.raiz)
        return self.preOrdenAux(self.raiz, l)

    def preOrdenAux(self, nodo, l):
        
            if not (nodo.izquierdo is None) and nodo.izquierdo not in l:
                l.append(nodo.izquierdo)
                self.preOrdenAux(nodo.izquierdo, l)
            elif not (nodo.derecho is None) and nodo.derecho not in l:
                l.append(nodo.derecho)
                self.preOrdenAux(nodo.derecho, l)
            elif not (nodo.padre is None):
                self.preOrdenAux(nodo.padre, l)

            return l

    def inOrden(self):
        l = list()
        return self.inOrdenAux(self.raiz, l)

    def inOrdenAux(self, nodo, l):
        
            if not (nodo.izquierdo is None) and nodo.izquierdo not in l:
                self.inOrdenAux(nodo.izquierdo, l)
            else:
                if nodo not in l:
                    l.append(nodo)
                if not (nodo.derecho is None) and nodo.derecho not in l:
                    self.inOrdenAux(nodo.derecho, l)
                elif not (nodo.padre is None):
                    self.inOrdenAux(nodo.padre, l)

            return l

    def postOrden(self):
        l = list()
        return self.postOrdenAux(self.raiz, l)

    def postOrdenAux(self, nodo, l):
        
            if not (nodo.izquierdo is None) and nodo.izquierdo not in l:
                self.postOrdenAux(nodo.izquierdo, l)
            elif not (nodo.derecho is None) and nodo.derecho not in l:
                self.postOrdenAux(nodo.derecho, l)
            elif not (nodo.padre is None):
                l.append(nodo)
                self.postOrdenAux(nodo.padre, l)
            else: l.append(nodo)

            return l

