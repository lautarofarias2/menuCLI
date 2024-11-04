class Menu():

    def __init__(self):
        self._productos = []

    def menu(self):
        while op < 3:
            print("\f\f--Menu--")
            print("Opcion 1: Ingresar producto")
            print("Opcion 2: Eliminar producto")
            print("Opcion 3: Actualizar stock")
            print("Opcion 4: Productos con poco stock")
            print("Opcion 5: Mostrar todos los productos")
            print("Opcion 6: Salir del menu")

            op = int(input("Ingrese una opcion: "))
            if op < 6:
                if op == 1:
                    self.cargarProducto()
                elif op == 2:
                    self.eliminarProducto()
                elif op == 3:
                    self.actualizarStock()
            else:
                print("opcion invalida")

    def actualizarStock():
        print("\f\f--Actualizar stock--")
        print("Opcion 1: Aumentar stock")
        print("Opcion 2: Reducir stock")
        print("Opcion 3: Cancelar")
        opTres = int(input("Ingrese una opcion"))
        prod = input("Producto a actualizar stock: ")
        cant = int(input("Cantidad a actualizar"))