from collections import Counter

# https://alexbarter.com/statistics/index-of-coincidence/
texto_cifrado = input("Introduce la palabra cifrada con Vigenere sin espacis y sin carácteres que no sean letras: ").upper()
icpromedio = input("¿Cuál es el IC promedio del idioma? ")

def calcular_ic(texto):
    N = len(texto)
    frecuencias = Counter(texto)
    suma_frecuencias = sum(f * (f - 1) for f in frecuencias.values())
    IC = suma_frecuencias / (N * (N - 1)) if N > 1 else 0
    return IC

def dividir_en_grupos(texto, longitud_clave):
    grupos = ['' for _ in range(longitud_clave)]
    for i, letra in enumerate(texto):
        grupos[i % longitud_clave] += letra
    return grupos

def analizar_longitud_clave(texto, max_longitud=20):
    resultados = {}
    for longitud in range(1, max_longitud + 1):
        grupos = dividir_en_grupos(texto, longitud)
        IC_promedio = sum(calcular_ic(grupo) for grupo in grupos) / longitud
        resultados[longitud] = IC_promedio
    return resultados

max_longitud = 12  # Máxima longitud que consideraremos
resultados_ic = analizar_longitud_clave(texto_cifrado, max_longitud)

print("\nResultados de IC por longitud de clave:")
for longitud, ic in resultados_ic.items():
    print(f"Longitud {longitud}: IC promedio = {ic:.4f}")

# Determina la longitud de clave más probable
longitud_probable = min(resultados_ic, key=lambda x: abs(resultados_ic[x] - float(icpromedio)))
print(f"\nLa longitud de clave más probable es: {longitud_probable}\n")
    

