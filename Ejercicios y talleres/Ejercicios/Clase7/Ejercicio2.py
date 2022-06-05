"""
A un trabajador le pagan según sus horas trabajadas por una 
tarifa de pago por hora. Si la cantidad de horas trabajadas 
es mayor 40 horas. La tarifa se incrementa en un 50% para las
horas extras. Calcular el salario del trabajador dadas las 
horas trabajadas y la tarifa ingresadas por el usuario.
"""

tarifa = input("Digite la tarifa de pago por horas: ")
horas = input("Digite horas trabajadas: ")

tarifa = int(tarifa)
horas = float(horas)

if horas > 40:
    extras = horas - 40
    salario = tarifa*(40 + extras*1.5)
else:
    salario = tarifa*horas

print("El salario del trabajador es:", salario)
 