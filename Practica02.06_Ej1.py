# Divisas
divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ").strip()

if divisa_input in divisas:
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    print("La divisa ingresada no está en el diccionario.")
