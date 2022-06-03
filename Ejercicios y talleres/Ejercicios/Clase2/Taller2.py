"""
Reto 2: ¿Cuánto costará el teléfono?

El IVA es un Impuesto sobre el Valor Añadido de un servicio o producto.
En España disponemos de varios tipos de IVA (21%, 10% y 4%). 
Este impuesto grava sobre el precio neto del producto, es decir, el
precio total o bruto corresponde al precio neto del producto más el 
impuesto que se le aplica.

"""
# Datos de entrada

costo_movil = 420
porcentaje = 20

# Proceso

total = costo_movil*(1+(20/100))

# Salida

print("El valor del telefono entoces es", total , "euros")
