agenda = {}

def agregar_contacto(nombre,telefono,correo):
    agenda[nombre] = {"telefono":telefono, "correo":correo}
    print("contacto agregado correctamente")

def buscar_contacto(nombre):
    if nombre in agenda:
        print("--- CONTACTO ---")
        print(f"nombre: {nombre}, telefono: {agenda[nombre]['telefono']}, correo: {agenda[nombre]['correo']}")
    else:
        print("contacto no encontrado")

def mostrar_contacto():
    print("--- LISTA DE CONTACTOS ---")
    for nombre, datos in agenda.items():
        print(f"nombre: {nombre}, telefono: {datos['telefono']}, correo: {datos['correo']}")

while True:
    print("--- MENU ---")
    print("1. agregar contacto")
    print("2. buscar contacto")
    print("3. mostrar lista de contactos")
    print("4. salir")

    op = input("que opcion elije ")

    if op == "1":
        nombre = input("nombre del contacto ")
        telefono = input("numero de telefono del contacto ")
        correo = input("correo electronico del contacto ")
        agregar_contacto(nombre,telefono,correo)
    elif op == "2":
        buscar = input("nombre del contacto que busca ")
        buscar_contacto(buscar)
    elif op == "3":
        mostrar_contacto()
    elif op == "4":
        break
    else:
        print("opcion no encontrada")