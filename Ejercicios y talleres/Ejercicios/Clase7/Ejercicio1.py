def par(n: int) -> str: 
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


def npar(n: int) -> str:
    """
    Leer un número entero de dos dígitos y determinar si ambos
    dígitos son pares.
    """
    # Validar parametros
    if type(n) != int:  
        return "Numero de entrada no es entero"
    
    n = str(n)
    if len(n) > 2:
        return "Numero de entrada debe ser de dos cifras"
     
    # Procesamiento
    nd = int(n[0])
    nu = int(n[1])

    mensajed = par(nd)
    mensajeu = par(nu)

    return f"{mensajed} y {mensajeu.lower()}"

print(npar(95))
    
