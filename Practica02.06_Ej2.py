# productos
precios = {
    'pan': 1.40,
    'huevos': 2.30,
    'cebolla': 0.85,
    'aceite': 4.35
}


articulo = input("Introduce el nombre del artículo: ").strip().lower()
cantidad = input("Introduce el número de unidades: ").strip()

if cantidad.isdigit():
    cantidad = int(cantidad)

    if articulo in precios:
        total = precios[articulo] * cantidad
        print(f"El precio total de {cantidad} {articulo}(s) es: {total:.2f}€")
    else:
        print("El artículo no está en la lista de precios.")
else:
    print("Por favor, introduce un número válido de unidades.")
