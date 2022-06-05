"""
Los teléfonos de una empresa tienen el siguiente formato 
prefijo-número-extension donde el prefijo es el código del 
país +57, y la extensión tiene dos dígitos (por ejemplo 
+57-313724710-56). Escribir un programa que pregunte por 
un número de teléfono con este formato y muestre por pantalla 
el número de teléfono sin el prefijo y la extensión.
"""

telefono = input("Digite su trlrfono Prefijo-número-extensión: \n")
L_telefono = telefono.split("-")

print("Su teléfono es: ", L_telefono[1])

 