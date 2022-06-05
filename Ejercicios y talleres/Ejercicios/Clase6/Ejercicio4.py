def par(n: int) -> str:
    """
    Diseñe un algoritmo que determina si un número es par o impar.
    Recuerde que un número es par si el resto de una división 
    entera con el número 2 es cero.
    """
    # Validar parametros
    if type(n) != int:  
        return "Numero de entrada no es entero"
    # Procesamiento
    if n % 2 == 0:
        mensaje = f"El numero {n} es par"
    else :
        mensaje = f"El numero {n} es impar"
    #salida
    return f"{mensaje}"
    
print(par(6))