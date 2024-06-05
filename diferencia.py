def diferencia():
    actual =  1.5
    minimo = 2.5
    maximo = 7
    promedio = 4
    crudo_actual = 3.5
    crudo = 5

    print("--------------------------------------------------------------------")
    diferencia_entre_actual_minimo = 100 - actual / minimo * 100
    print(f"la diferencia entre actual y minimo es {diferencia_entre_actual_minimo}%")
    print("--------------------------------------------------------------------")
    #se multiplica por mil y se divide emtre 10 para que no se pase el numero con los flotantes y mover la coma
    diferencia_entre_actual_maximo = 100 - actual * 1000 // maximo /10
    print(f"la deferencia entre actual y maximo es {diferencia_entre_actual_maximo}%")
    print("--------------------------------------------------------------------")
    diferencia_entre_actual_promedio = 100 - actual / promedio * 100
    print(f"la diferencia entre actual y el promedio es {diferencia_entre_actual_promedio}%")
    print("--------------------------------------------------------------------")
    porcentaje_entre_promedio_crudo = 100 - promedio / crudo *100
    print(f"porcentaje basura que se reduse en el crudo {porcentaje_entre_promedio_crudo}%")
    print("--------------------------------------------------------------------")
    porcentaje_entre_actual_crudo_actual = 100 - actual * 1000 // crudo_actual / 10
    print(f"porcentaje basura que se reduse en el crudo actual {porcentaje_entre_actual_crudo_actual}%")
    print("--------------------------------------------------------------------")
    diferencia_entre_promedio_actual = promedio * 100 // actual / 10
    print(f"la diferencia entre promedio y actual es {diferencia_entre_promedio_actual}")
    print("--------------------------------------------------------------------")
    diferencia_entre_actual_promedio = actual * 100 // promedio / 10
    print(f"la diferencia entre actual y promedio es {diferencia_entre_actual_promedio}%")
    print("--------------------------------------------------------------------")

def otro():
    print("ingrese una frase o un texto")
    texto = input("")
    palabras = texto.split(" ")
    contadas = len(palabras)
    print(f"dijiste {contadas} palabras y demoraste {contadas/2} segundos en decirlo")
    print(f"yo tarde {contadas*100//2*0.50/100} segundos en decirlo")
    if contadas >= 120 :
        print("escribes mucho")

while True:
    print("opcion 1 difrencias")
    print("opcion 2 contador de palabras")
    print("opcion 3 salir")

    op = input("elija una opcion ")

    if op == "1":
        diferencia()
    elif op == "2":
        otro()
    elif op == "3":
        break
    else:
        print("no se encontro la opcion")