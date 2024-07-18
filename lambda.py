def obtener(cantidad):
    personas = []
    for i in range(cantidad):
        nombre = input("ingrese su nombre ")
        edad = int(input("ingrese su edad "))
        persona = (nombre,edad)
        personas.append(persona)
    personas.sort(key=lambda x:x[1])
    mayor = personas[-1][0]
    menor = personas[0][0]
    return mayor,menor

persona_mayor,persona_menor = obtener(3)
print(f"el mayor es {persona_mayor} y el menor es {persona_menor} ")