"""
Reto 3: ¿Cuántas vueltas dará un Fidget Spinner?

El spinner es un juguete que cabe en la palma de la mano y consiste en 
tres aros unidos entre sí. En el centro hay un círculo que hace las 
veces de eje giratorio y permite que los aros de vueltas y más vueltas, 
como las hélices de un helicóptero.

Sabemos que un Fidget Spinner da 147 vueltas por minuto ¿Cuántas vueltas 
dará en 640 segundos? Para este ejercicio se desprecia el rozamiento con 
el aire.

"""
# Datos de entrada

vueltas_por_minuto = 147
tiempo_segundos = 640

# Proceso

vueltas = vueltas_por_minuto*(tiempo_segundos/60)

# Salida

print("Las vuetas dadas en", tiempo_segundos , "segundos es", vueltas , "vueltas")