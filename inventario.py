productos = {}

def agregar_producto(nombre,cantidad):
    productos[nombre] = {"cantidad":cantidad}
    print("producto agregado correctamente")

def mostrar_producto(nombre):
    if nombre in productos:
        print(f"{nombre}: {productos[nombre]['cantidad']}")
    else:
        print("no se encontro el producto")

def lista():
    print("|||lista de productos|||")
    for nombre,datos in productos.items():
        print(f"{nombre}: {datos['cantidad']}")

while True:
    print("°°°MENU°°°")
    print("1 agregar producto")
    print("2 buscar producto")
    print("3 lista de productos")
    print("3 salir")
    op = input("")

    if op == "1":
        nombre = input("ingrese el producto ")
        cantidad = int(input("ingrese la cantidad de productos "))
        agregar_producto(nombre,cantidad)
    elif op == "2":
        nombre = input("ingrese el nombre del producto que desea buscar ")
        mostrar_producto(nombre)
    elif op == "3":
        lista()
    elif op == "4":
        break
    else:
        print("no se encontro la opcion")
