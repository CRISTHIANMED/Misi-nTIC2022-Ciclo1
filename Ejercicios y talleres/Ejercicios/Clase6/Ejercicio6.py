def intervalo(n: float) -> str:
    """
    Diseñe un algoritmo que determine si un número real (x) se 
    encuentra dentro de uno de los siguientes rangos: (3.5, 7.8], 
    [9.3, 14.5) y [23.4, 45.3].
    """
    # Validar parametros
    # Procesamiento
    if n > 3.5 and n <= 7.8:
        mensaje = f"El numero {n} es esta en el intervalo (3.5, 7.8]"
    elif n >= 9.3 and n < 14.5:
        mensaje = f"El numero {n} es esta en el intervalo (9.3, 14.5]"
    elif n >= 23.4 and n <= 45.3:
        mensaje = f"El numero {n} es esta en el intervalo [23.4, 45.3]"
    else:
        mensaje = f"El numero {n} no esta en nigun intervalo"
    #salida
    return f"{mensaje}"
    
print(intervalo(23.4))