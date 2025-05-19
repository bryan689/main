historial = []

def suma(numero1,numero2):
    resultado = numero1 + numero2
    historial.append(f"{numero1} + {numero2} = {resultado}")
    print(f"el resultado es {resultado}")

def resta(numero1,numero2):
    resultado = numero1 - numero2
    historial.append(f"{numero1} - {numero2} = {resultado}")
    print(f"el resultado es {resultado}")

def multiplicacion(numero1,numero2):
    resultado = numero1 * numero2
    historial.append(f"{numero1} x {numero2} = {resultado}")
    print(f"el resultado es {resultado}")

def division(numero1,numero2):
    if numero2 != 0:
        resultado = numero1 / numero2
        historial.append(f"{numero1} / {numero2} = {resultado}")
        print(f"el resultado es {resultado}")
    else:
        print("no se puede dividir entre 0")
        historial.append(f"{numero1} / {numero2} = error (no se puede dividri entre 0)")


while True:
    print("-*-*-*-*MENU*-*-*-*")
    print("que operacion desea elegir")
    print("suma: +")
    print("resta: -")
    print("multiplicacion: *")
    print("division: /")
    print("historial: historial")
    print("salir")
    op = input("").lower()
    
    if op == "+":   
        while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                suma(numero1,numero2)
                break
            except ValueError:
                print("ingrese solo numeros")
    elif op == "-":
        while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                resta(numero1,numero2)
                break
            except ValueError:
                print("ingrese solo numeros")
    elif op == "*":
        while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                multiplicacion(numero1,numero2)
                break
            except ValueError:
                print("ingrese solo numeros")
    elif op == "/":
        while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                division(numero1,numero2)
                break
            except ValueError:
                print("ingrese solo numeros")
    elif op == "historial":
        if historial:
            print("-*-*-*HISTORIAL*-*-*-")
            for operacion in historial:
                print(operacion)
        else:
            print("-*-*-*HISTORIAL*-*-*-")
            print("no hay operaciones registradas")
    elif op == "salir":
        break
    else :
        print("no se encontro la operacion")   
