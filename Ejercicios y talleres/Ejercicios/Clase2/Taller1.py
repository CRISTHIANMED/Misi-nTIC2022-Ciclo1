"""
# Reto 1: Los cinco doses

¿Sabrías obtener los números del 0 al 10 utilizando cinco 2's y 
los signos suma (+), resta (-), multiplicación (x) y división (/) y 
paréntesis? Te regalamos el ejemplo para el 0 y el resto deberás 
calcularlos tú mismo y comprobarlos en Python. ¡Ánimo!

"""
# Datos de entrada

# Proceso
V0 = (2-2)*2*2*2
V1 = int(2+2-2-(2/2))
V2 = 2+2-2+2-2
V3 = int((2/2)+2-2+2)

# Salida

print("El valor para (2-2)*2*2*2 = ", V0)
print("El valor para 2+2-2-(2/2) = ", V1)
print("El valor para 2+2-2+2-2 = ", V2)
print("El valor para (2/2)+2-2+2 = ", V3)
