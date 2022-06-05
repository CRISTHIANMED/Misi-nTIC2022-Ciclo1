def nota_definitiva(nota: float) -> str:
    """
   Diseñe un algoritmo que permita imprimir un mensaje según la 
   nota definitiva de un estudiante entre 0.0 y 5.0, de acuerdo 
   con la Tabla:

   < 3.0 Insuficiente
   <= 3.5 Aceptable
   <= 4.0 Sobresaliente
   <= 5.0 Excelente
    """
    # Validar parametros
    if nota < 0.0 or nota > 5:  
        return "Su nota definitiva debe estar entre 0.0 y 5.0"
    # Procesamiento
    if nota >= 0 and nota < 3.0:
        mensaje = "Insuciente"
    elif nota >= 3.0 and nota <= 3.5:
        mensaje = "Aceptable"
    elif nota > 3.5 and nota <= 4.0:
        mensaje = "sobresaliente"
    elif nota > 4 and nota <= 5:
        mensaje = "Excelente"
    #salida
    return f"Su nota es {mensaje}"
    
        
print(nota_definitiva(0))