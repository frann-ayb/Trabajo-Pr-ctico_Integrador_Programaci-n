class Producto:   #permite crear nuevos productos (objetos) con datos dados por el usuario
    def __init__(self, codigo, nombre, cantidad, precio):
        self.nombre = nombre    #se asigna un nombre al producto
        self.cantidad = cantidad    #se asigna una cantidad al producto
        self.precio = precio    #se asigna un precio al producto
        self.codigo = codigo    #se asigna un codigo al producto
        self.izquierda = None   #se crea una referencia para un futuro nodo hijo izquierdo
        self.derecha = None     #se crea una referencia para un futuro nodo hijo derecho

class ArbolBinario:     #permite crear un arbol binario para almacenar productos (nodos - objetos)
    def __init__(self):
        self.referencia = None  #se crea la referencia al primer nodo del arbol(raiz)

    def insertar(self, codigo, nombre, cantidad, precio):   #se reciben los datos dados por el usuario
        self.referencia = self.insertar_recursivo(self.referencia, codigo, nombre, cantidad, precio)    #se asigna el valor return de la funcion a la referencia.

    def insertar_recursivo(self, nodo, codigo, nombre, cantidad, precio):   #recibe los datos
        if nodo is None:        #si la referencia esta vacia
            return Producto(codigo, nombre, cantidad, precio)   #se crea un nuevo producto
        if codigo < nodo.codigo:        #si ya existe un nodo padre se añadiran nodos hijo izquierdos o derechos
            nodo.izquierda = self.insertar_recursivo(nodo.izquierda, codigo, nombre, cantidad, precio)  #llama recursivamente
        elif codigo > nodo.codigo:
            nodo.derecha = self.insertar_recursivo(nodo.derecha, codigo, nombre, cantidad, precio)      #llama recursivamente
        return nodo     #return nodo con hijo asignado

    def buscar(self, codigo):
        return self.buscar_recursivo(self.referencia, codigo) #se envia el nodo raiz y el codigo

    def buscar_recursivo(self, nodo, codigo):   #busca el nodo a partir del codigo dado
        if nodo is None:        #se llego a un nodo hoja o el nodo raiz esta vacio (el nodo buscado no existe)
            return None
        if codigo == nodo.codigo:   #se compara el codigo del nodo actual y el codigo del nodo buscado
            return nodo             #devuelve el nodo buscado si es encontrado
        elif codigo < nodo.codigo:      #recorre el arbol hacia el hijo izq del nodo actual
            return self.buscar_recursivo(nodo.izquierda, codigo)
        else:                           #recorre el arbol hacia el hijo der del nodo actual
            return self.buscar_recursivo(nodo.derecha, codigo)

    def modificar(self, prod, nombre, cantidad, precio):##permite modificar nodos existentes
        
            prod.nombre = nombre        #asigna el nuevo nombre dado
            prod.cantidad = cantidad    #asigna la nueva cantidad dada
            prod.precio = precio        #asigna el nuevo precio dado
            return True
        


def mostrar_menu():     #funcion que permite imprimir el menu de opciones
    print("\n----TP-Integrador---- MENÚ ----")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Modificar producto")
    print("4. Salir")
    print("--------------------------------")

arbol = ArbolBinario() 
# Se crean productos de ejemplo
arbol.insertar(10, "computadora escritorio", 8, 1200) # (codigo de producto, "nombre", cantidad, precio)
arbol.insertar(11, "tv smart vision 60p 4k", 22, 1000)
arbol.insertar(15, "disco SSD 2tb", 18, 2200)

estado_programa = True
while estado_programa:         #estructura repetitiva que permite siempre volver al menu principal hasta que el usuario finalice el programa
    mostrar_menu() #se llama a la funcion mostrar_menu
    opcion = input("Seleccione una opción: ") #se solicita la opcion al usuario

        #se ejecuta la opcion elegida a partir de de una estructura if
    if opcion == "1":       #opción: crear producto
        try:                                                            #maneja errores en el ingreso de datos
            codigo = int(input("Ingrese código del producto (número entero): "))        #solicta el codigo del producto
            prod = arbol.buscar(codigo)                                                 #busca si el código ingresado existe en el arbol
            if prod:                                                                    #si el código pertenece a otro producto
                print(f"\nEl codigo ingresado ya pertenece a un producto existente: {prod.nombre}")
            else:                                                                       #si el código esta disponible
                nombre = input("Ingrese nombre del producto: ")                             #solicta el nombre del producto
                cantidad = int(input("Ingrese cantidad del producto (número entero): "))    #solicta la cantidad del producto
                precio = float(input("Ingrese precio del producto(sin '$'): "))             #solicta el precio del producto
                arbol.insertar(codigo, nombre, cantidad, precio)                            #envia todos los datos ingresados la funcion insertar
                print("\nProducto agregado con éxito: ")
                prod = arbol.buscar(codigo)                                 #muestra el producto creado a partir de la funcion buscar
                print(f"Código: {prod.codigo}")
                print(f"Nombre: {prod.nombre}")
                print(f"Cantidad: {prod.cantidad}")
                print(f"Precio: ${prod.precio}")
        except ValueError:                                              #mensaje en caso de error
            print("Ingrese datos validos.")

    elif opcion == "2":     #opción: buscar producto
        try:                                                            #maneja errores en el ingreso de datos
            codigo = int(input("Ingrese código del producto a buscar: "))   #solicita el codigo asociado al producto buscado
            prod = arbol.buscar(codigo)                                     #llama a la funcion buscar enviando el codigo
            if prod:                                                        #muestra los atributos si existe el producto
                print(f"\nProducto encontrado:")
                print(f"Código: {prod.codigo}")
                print(f"Nombre: {prod.nombre}")
                print(f"Cantidad: {prod.cantidad}")
                print(f"Precio: ${prod.precio}")
            else:                                                           #cuando el producto no es encontrado
                print("Producto no encontrado.")
        except ValueError:                                              #mensaje en caso de error
            print("Ingrese datos validos.")

    elif opcion == "3":     #opción: modificar producto
        try:                                                            #maneja errores en el ingreso de datos
            codigo = int(input("Ingrese código del producto a modificar: "))    #solicita el codigo asociado al producto a modificar
            prod = arbol.buscar(codigo)                                         #identifica la existencia del producto y sus atributos
            if prod:                                                            #si existe solicita los nuevos atributos (excepto el código de producto)
                nombre = input(f"Nuevo nombre (actual: {prod.nombre}): ")
                cantidad = int(input(f"Nueva cantidad (actual: {prod.cantidad}): "))
                precio = input(f"Nuevo precio (actual: {prod.precio}): ")
                arbol.modificar(prod, nombre, cantidad, precio) #opcion de enviar el "prod" y no el "codigo"
                print("Producto modificado con exito.")
            else:                                                               #en caso de que el producto no exista
                print("Producto no encontrado.")
        except ValueError:                                              #mensaje en caso de error
            print("Ingrese datos validos.")

    elif opcion == "4":     #opción: salir
        print("Saliendo del programa...")
        estado_programa = False      #finaliza el ciclo while y termina el programa
    else:
        print("ingrese una de las opciones disponibles.")   #cuando el usuario ingresa valores invalidos
