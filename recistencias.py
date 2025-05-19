color_codes = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
}

multiplier_codes = {
    "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10000,
    "green": 100000, "blue": 1000000, "gold": 0.1, "silver": 0.01
}

tolerance_codes = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25, "violet": 0.1,
    "gray": 0.05, "gold": 5, "silver": 10
}

def colors_to_resistance(color1, color2, multiplier, tolerance):
    try:
        color1, color2, multiplier, tolerance = color1.lower().strip(), color2.lower().strip(), multiplier.lower().strip(), tolerance.lower().strip()
        if color1 not in color_codes or color2 not in color_codes or multiplier not in multiplier_codes or tolerance not in tolerance_codes:
            return "Error: Color inválido. Verifique los valores ingresados."
        
        value = (color_codes[color1] * 10 + color_codes[color2]) * multiplier_codes[multiplier]
        tolerance_value = tolerance_codes[tolerance]
        
        return f"Resistencia: {value}Ω ± {tolerance_value}%"
    except Exception as e:
        return f"Error: {e}"

def resistance_to_colors(resistance, tolerance):
    try:
        resistance_str = str(int(resistance))
        tolerance = float(tolerance)
        
        if len(resistance_str) < 2 or tolerance not in tolerance_codes.values():
            return "Error: Valor inválido. Asegúrese de ingresar una resistencia válida y una tolerancia aceptada."
        
        first_digit = int(resistance_str[0])
        second_digit = int(resistance_str[1])
        multiplier = len(resistance_str) - 2
        
        color1 = list(color_codes.keys())[list(color_codes.values()).index(first_digit)]
        color2 = list(color_codes.keys())[list(color_codes.values()).index(second_digit)]
        multiplier_color = list(multiplier_codes.keys())[list(multiplier_codes.values()).index(10**multiplier)]
        tolerance_color = list(tolerance_codes.keys())[list(tolerance_codes.values()).index(tolerance)]
        
        return f"Colores: {color1}, {color2}, {multiplier_color}, {tolerance_color}"
    except Exception as e:
        return f"Error: {e}"

def main():
    while True:
        print("\nMenú:")
        print("1. Convertir código de colores a resistencia")
        print("2. Convertir resistencia a código de colores")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            c1 = input("Ingrese el primer color: ")
            c2 = input("Ingrese el segundo color: ")
            m = input("Ingrese el color del multiplicador: ")
            t = input("Ingrese el color de la tolerancia: ")
            print(colors_to_resistance(c1, c2, m, t))
        
        elif opcion == "2":
            try:
                r = int(input("Ingrese el valor de la resistencia en Ohmios: ").strip())
                t = float(input("Ingrese la tolerancia en %: ").strip())
                print(resistance_to_colors(r, t))
            except ValueError:
                print("Error: Ingrese valores numéricos válidos.")
        
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()
