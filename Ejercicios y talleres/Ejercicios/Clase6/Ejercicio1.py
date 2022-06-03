# Diseñe un algoritmo que reciba una nota definitiva entre 0.0 y 5.0. 
# El algoritmo debe imprimir el valor ingresado, y de ser una nota mayor 
# o igual a 4.0, deberá imprimir un mensaje de felicitaciones

def nota_definitiva(nota: float) -> str:
    # Validar parametros
    # not(nota >= 0.0 and nota <= 5)
    if nota < 0.0 or nota > 5: # ¬(p and q) -> ¬p or ¬q 
        return "Su nota definitiva debe estar entre 0.0 y 5.0"
    # Procesamiento
    if nota >= 4.0:
        mensaje = "¡¡Felicitaciones!!"
    else :
        mensaje = ""
    #salida
    return f"Su nota es {nota} {mensaje}"
    
        
print(nota_definitiva(4.5))