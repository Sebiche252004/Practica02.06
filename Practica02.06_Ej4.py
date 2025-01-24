# personas

persona = {}

datos = ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']

for dato in datos:
    valor = input(f"Introduce tu {dato}: ").strip()
    persona[dato] = valor  
    print("Diccionario actualizado:", persona) 

print("\nInformación final de la persona:")
for clave, valor in persona.items():
    print(f"{clave.capitalize()}: {valor}")

