def factorial(n):
    # Validar
    if n < 0:
        return "Número erróneo"
    # Algoritmo
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))