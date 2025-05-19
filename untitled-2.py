historial = []
def suma():
    while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                resultado = numero1 + numero2
                print(f"el resultado es {resultado}")
                historial.append(f"{numero1} + {numero2} = {resultado}")
                break
            except ValueError:
                print("ingrese solo numeros")

def resta():
    while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                resultado = numero1 + numero2
                print(f"el resultado es {resultado}")
                historial.append(f"{numero1} - {numero2} = {resultado}")
                break
            except ValueError:
                print("ingrese solo numeros")

def multiplicacion():
    while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                resultado = numero1 + numero2
                print(f"el resultado es {resultado}")
                historial.append(f"{numero1} x {numero2} = {resultado}")
                break
            except ValueError:
                print("ingrese solo numeros")

def division():
    while True:
            try:
                numero1 = int(input("ingrese el primer numero "))
                numero2 = int(input("ingrese el segundo numero "))
                if numero2 != 0:
                    resultado = numero1 + numero2
                    print(f"el resultado es {resultado}")
                    historial.append(f"{numero1} / {numero2} = {resultado}")
                    break
                else:
                    print("no se puede dividir entre 0 pendejo")
                    historial.append(f"{numero1} / {numero2} = sytans error xd (no se puede dividir entre cero pendejo)")
            except ValueError:
                print("ingrese solo numeros")
    

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
        suma()
           
    elif op == "-":
       resta()
    elif op == "*":
        multiplicacion()
    elif op == "/":
       division()
    elif op == "historial":
        if historial:
             print("-*-*-*HISTORIAL*-*-*-")
             for operaciones in historial:
                  print(operaciones)
        else:
             print("-*-*-*HISTORIAL*-*-*-")
             print("no se encontro registro en el historial")
    elif op == "salir":
        break
    else :
        print("no se encontro la operacion")   