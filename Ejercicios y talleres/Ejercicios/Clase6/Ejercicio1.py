def nota_definitiva(nota: float) -> str:
    """
    Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. 
    El algoritmo debe imprimir el valor ingresado, y de ser una nota
    mayoro igual a 4.0, deberá imprimir un mensaje de felicitaciones

    """
    # Validar parametros
    if nota < 0.0 or nota > 5:  
        return "Su nota definitiva debe estar entre 0.0 y 5.0"
    # Procesamiento
    if nota >= 4.0:
        mensaje = "¡¡Felicitaciones!!"
    else :
        mensaje = ""
    #salida
    return f"Su nota es {nota} {mensaje}"
    
        
print(nota_definitiva(4.5))