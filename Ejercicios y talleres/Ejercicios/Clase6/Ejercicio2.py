def nota_definitiva(nota: float) -> str:
    """
    Diseñe un algoritmo que reciba una nota definitiva entre 0.0 
    y 5.0. El algoritmo debe imprimir el valor ingresado, y un 
    mensaje que indique si el estudiante “Ganó el curso” o 
    “Perdió el curso”. Se gana el curso solo si la nota definitiva 
    es mayor o igual a 3.0.

    """
    # Validar parametros
    if nota < 0.0 or nota > 5:  
        return "Su nota definitiva debe estar entre 0.0 y 5.0"
    # Procesamiento
    if nota >= 3.0:
        mensaje = "Gano el curso"
    else :
        mensaje = "Perdio el curso"
    #salida
    return f"{mensaje}"
    
        
print(nota_definitiva(4.5))