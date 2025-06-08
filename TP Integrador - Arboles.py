class Producto:
    def __init__(self,codigo, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.codigo = codigo
        self.izquierda = None
        self.derecha = None
        
class ArbolBinario:
    def __init__(self):
        self.referencia = None

    def insertar(self, codigo, nombre, cantidad, precio):
        self.referencia = self.insertar_recursivo(self.referencia, codigo, nombre, cantidad, precio)

    def insertar_recursivo(self, nodo, codigo, nombre, cantidad, precio):
        if nodo is None:
            nodo = Producto(codigo, nombre, cantidad, precio)
        if codigo < nodo.codigo:
            nodo.izquierda = self.insertar_recursivo(nodo.izquierda, codigo, nombre, cantidad, precio)
        elif codigo > nodo.codigo:
            nodo.derecha = self.insertar_recursivo(nodo.derecha, codigo, nombre, cantidad, precio)
        return nodo


    
arbol = ArbolBinario()
arbol.insertar(10, "manzana", 8, "$1200")
arbol.insertar(11, "pera", 22, "$1000")
arbol.insertar(15, "anana", 18, "$2200")


