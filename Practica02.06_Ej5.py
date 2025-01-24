# Epañol-ingles
traducciones = {}

print("Introduce palabras en el formato 'español:inglés'. Escribe 'terminar' para finalizar.")
while True:
    entrada = input("Introduce una palabra y su traducción: ").strip().lower()
    if entrada == "terminar":
        break
    if ':' in entrada:
        esp, ing = entrada.split(':', 1)
        traducciones[esp.strip()] = ing.strip()
    else:
        print("Formato incorrecto. Usa el formato 'español:inglés'.")

print("\nDiccionario de traducción creado:")
print(traducciones)


frase = input("\nIntroduce una frase en español para traducir: ").strip().lower()

palabras = frase.split()
frase_traducida = []

for palabra in palabras:
    if palabra in traducciones:
        frase_traducida.append(traducciones[palabra])
    else:
        frase_traducida.append(palabra)

print("\nFrase traducida:")
print(' '.join(frase_traducida))

