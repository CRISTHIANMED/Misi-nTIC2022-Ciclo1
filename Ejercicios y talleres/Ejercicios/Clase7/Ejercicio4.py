"""
Escribir un programa que pregunte el nombre del usuario en la 
consola y un número entero e imprima por pantalla en líneas 
distintas el nombre del usuario tantas veces como el número 
introducido.
"""

nombre = input("Digite su nombre: ")
n = input("Digite un numero entero: ")
n = int(n)

print(f"\n{nombre}"*n)
 