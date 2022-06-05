"""
Diseñe un algoritmo que permita solicitar tanto el nombre como 
la edad de una persona y posteriormente indicar si es “Mayor de 
edad” o “Menor de edad” según la información ingresada. Una 
persona se considera mayor de edad si tiene 18 años o más.
"""
nombre = input("Ingrese su nombre: ")
if not nombre:  
    print("No ingreso nombre")
else:
    edad = input("Ingrese su edad: ")
    if not edad:
        print("No ingreso la edad")
    else:
        edad = int(edad)
        if edad <=0 : 
            print("Edad invalida")
        else:
            if edad >= 18:
                print(f"{nombre} es mayor de edad")
            else:
                print(f"{nombre} es menor de edad")


