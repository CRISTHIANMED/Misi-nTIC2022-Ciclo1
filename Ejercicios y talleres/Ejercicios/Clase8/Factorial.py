def factorial(n: int) -> int:
    resultado = 1
    numero_actual = 2
    while numero_actual <= n:
        resultado *= numero_actual 
        numero_actual += 1
    return resultado


print(factorial(5))