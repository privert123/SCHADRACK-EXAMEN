productos = {
    '8475HD': 'HP', '2175HD': 'lenovo', 'JjfFHD': 'Asus', 'fgdxFHD': 'Acer',
    '123FHD': 'lenovo', '342FHD': 'HP', 'GF75HD': 'MSI', 'UWU131HD': 'Dell', 'FS1230HD': 'Acer'
}

stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
}

def stock_marca(marca):
    marca = marca.lower()
    total_stock = 0
    for modelo in productos:
        if productos[modelo].lower() == marca:
            total_stock += stock[modelo][1]
    print(f"El stock es: {total_stock}")

def busqueda_precio(p_min, p_max):
    resultado = []
    for modelo in stock:
        precio, cant = stock[modelo]
        if p_min <= precio <= p_max and cant > 0:
            resultado.append(f"{productos[modelo]}--{modelo}")
    if resultado:
        resultado.sort()
        print("Los notebooks entre los precios consultas son:", resultado)
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")

        if opcion == '1':
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)

        elif opcion == '2':
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
            busqueda_precio(p_min, p_max)

        elif opcion == '3':
            while True:
                modelo = input("Ingrese modelo a actualizar: ")
                try:
                    nuevo_precio = int(input("Ingrese precio nuevo: "))
                    actualizado = actualizar_precio(modelo, nuevo_precio)
                    if actualizado:
                        print("Precio actualizado!!")
                    else:
                        print("El modelo no existe!!")
                except ValueError:
                    print("Debe ingresar un precio válido!!")
                otra = input("Desea actualizar otro precio (s/n)?: ").lower()
                if otra != 's':
                    break

        elif opcion == '4':
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción válida!!")
menu()

