
## 1. Extrae vocales del mensaje

mensaje = "HolA, comO estAs tu?"
vocales = 'aeiou'
for letra in mensaje:
     if letra.lower() in vocales:
            print(letra, end=" ")

print("\n")

## 2. Extrae consonantes del mensaje
mensaje2 = "Hola, como estas tu?"
vocales2 = 'aeiou'
for letra2 in mensaje2:
     if letra2 not in vocales2 and letra2.isalpha():
            print(letra2, end=" ")



