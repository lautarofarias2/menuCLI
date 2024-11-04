#Menu

productos = [] #lista de productos
op = 0 #variable para guardar la opcion
idProd = 0 #variable para guardar el id
while op < 3:
    #muestra al usuario el menu con las opciones
    print("\f\f--Menu--")
    print("Opcion 1: Ingresar producto")
    print("Opcion 2: Mostrar productos cargados")
    print("Opcion 3: Salir")
    #variable para guardar la opcion elegida
    op = int(input("Ingrese una opcion: "))
    if op <= 3:
        #En caso de seleccionar la opcion 1
        if op == 1:
            #genera un id unico para cada producto a cargar
            idProd += 1
            #guarda el producto ingresado por el usuario en una lista
            prod = [input("Ingrese el producto: ")]
            #ingresa la cant de stock actual del prod en la lista del producto
            prod.append(int(input("Ingresar cantidad de stock: ")))
            #guarda el id en una lista y luego se enlaza en la lista producto
            prod.append(["id:", idProd])
            #guarda la lista producto en la lista de productos
            productos.append(prod)
        #En caso de elegir opcion 2
        elif op == 2:
            #si la lista de productos esta vacia
            if len(productos) == 0:
                print("No tiene productos cargados")
            #si la lista tiene al menos un producto
            else:
                i = 0
                while i < len(productos):
                    print("Producto " + str(i+1) + ": " + str(productos[i]))
                    i+=1
        #si se selecciona la opcion 3
        else:
            #imprime y sale del bucle
            print("Saliendo del menu")
    #en caso de seleccionar una opcion inexsistente
    else:
        print("Opcion invalida")