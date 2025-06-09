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

def pedir_datos_producto():
    continuar = "s"
    while continuar.lower() == "s":
            codigo = input("Por favor ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese que cantidad tiene de este producto: "))
            precio = int(input("Ingrese el precio del producto: "))
            arbol.insertar(codigo, nombre, cantidad, precio)
            print("¡Producto ingresado correctamente!\n")
            continuar = input("¿Desea ingresar otro producto? (s/n): ")
    print("\nRegresando al menú principal...\n")

def buscar_por_codigo(nodo, codigo):
    if nodo is None:
        return None
    if codigo == nodo.codigo:
        return nodo
    elif codigo < nodo.codigo:
        return buscar_por_codigo(nodo.izquierda, codigo)
    else:
        return buscar_por_codigo(nodo.derecha, codigo)
    
def buscar_por_nombre(nodo, nombre):
    if nodo is None:
        return None
    if nodo.nombre.lower() == nombre.lower():
        return nodo
    izquierda = buscar_por_nombre(nodo.izquierda, nombre)
    if izquierda:
        return izquierda
    derecha = buscar_por_nombre(nodo.derecha, nombre)
    return derecha

def busqueda():
    opcion = input("Para búscar productos por Código digita 1, por Nombre digita 2: ")
    if opcion == "1":
        codigo = input("Ingrese el Código del producto: ")
        resultado = buscar_por_codigo(arbol.referencia, codigo)
    elif opcion == "2":
        nombre = input("Ingrese el Nombre del producto: ")
        resultado = buscar_por_nombre(arbol.referencia, nombre)
    else:
        print("Opción invalida.\n")

    if resultado:
        print("¡Producto encontrado!\n")
        print(f"Código: {resultado.codigo} - Nombre: {resultado.nombre} - Cantidad: {resultado.cantidad} - Precio: ${resultado.precio}.\n")    
    else:
        print("Producto no encontrado.")
        
def menu():
    opcion = ""
    while opcion != "3":
        print("¡Bienvenid@ al módulo de ventas!")
        print("1. Insertar un producto")
        print("2. Consultar un producto")
        print("3. Salir del programa")
        opcion = input("Seleccione una opción para comenzar: ")

        if opcion == "1":
            pedir_datos_producto()
        elif opcion == "2":
            busqueda()
        elif opcion == "3":
            print("¡Hasta pronto!")
        else:
            print("Opción invalida, intente nuevamente.\n")
            
arbol = ArbolBinario()
menu()
#arbol.insertar(10, "manzana", 8, "$1200")
#arbol.insertar(11, "pera", 22, "$1000")
#arbol.insertar(15, "anana", 18, "$2200")


