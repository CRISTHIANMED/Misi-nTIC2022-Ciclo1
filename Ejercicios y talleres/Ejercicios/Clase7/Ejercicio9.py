def validar_cuadratica(a:float, b:float ,c:float) -> str:
     
    if a != 0 and (b**2-4*a*c) >=0:
        return "Ecuacion cuadratica tiene solucion"
    else:
        return "Ecuacion cuadratica no tiene solucion"

print(validar_cuadratica(0,8,1))

