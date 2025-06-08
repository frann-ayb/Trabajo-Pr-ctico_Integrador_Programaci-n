class nodo:
    def __init__(self, valor): #le pasamos un nodo con un valor
        nodo.valor = valor #ese valor se asigna a la relacion nodo.valor
        nodo.hijo_derecho = None #se define la existecia de hijos pero aun no su valor
        nodo.hijo_izquierdo = None 

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def asignar_raiz(self, nodo, valor):
        if self.raiz is None:
            self.raiz = nodo(valor) #se crea un nuevo nodo para la raiz
        else:
            self.insertar_nodos_izq_der(self.raiz, valor) #se envia el nodo y el valor a la funcion recursiva
    
    def insertar_nodos_izq_der(self, nodo_padre, valor):
        if valor < nodo_padre.valor: #valor hijo comparado al valor actual (valor del nodo padre)
            if nodo_padre.hijo_izquierdo is None:
                nodo_padre.hijo_izquierdo = nodo(valor)
            else:
                self.insertar_nodos_izq_der(nodo_padre.hijo_izquierdo, valor)
        else:
            if nodo_padre.hijo_derecho is None:
                nodo_padre.hijo_derecho = nodo(valor)
            else:
                self.insertar_nodos_izq_der(nodo_padre.hijo_derecho, valor)

