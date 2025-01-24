#datos
nombre = input("Introduce tu nombre: ").strip()
edad = input("Introduce tu edad: ").strip()
direccion = input("Introduce tu dirección: ").strip()
telefono = input("Introduce tu número de teléfono: ").strip()

datos_usuario = {
    'nombre': nombre,
    'edad': edad,
    'direccion': direccion,
    'telefono': telefono
}

print(f"{datos_usuario['nombre']} tiene {datos_usuario['edad']} años, vive en {datos_usuario['direccion']} y su número de teléfono es {datos_usuario['telefono']}.")
