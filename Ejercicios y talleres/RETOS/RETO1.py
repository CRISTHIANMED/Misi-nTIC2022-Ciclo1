def CDT(usuario: str , capital: int , Tiempo: int):

    """CDT;

    Parametros: 
      Usuario (str) : alfanumerico que identifica al usuario
      Capital (int) : Monto a ingresar 
      Tiempo (int) : Tiempo del CDT

    Salidad:
      String de la forma : "Para el usuario {} La cantidad de dinero a recibir,
      según el monto inicial  {} para un tiempo de {} meses es: {}"

    """

    cantidad = capital
    porcentaje_interes = 3/100
    porcentaje_perder = 2/100


    if Tiempo > 2 :
        valor_intereses = (cantidad*porcentaje_interes*Tiempo)/12
        valor_total = valor_intereses + cantidad 
    else :
        valor_perder = cantidad * porcentaje_perder
        valor_total = cantidad - valor_perder
        

    """
    return "Para el usuario " + usuario + " La cantidad de dinero a recibir, " \
           "según el monto inicial " + str(cantidad) + " para un tiempo de "\
           + str(Tiempo) + " meses es: " + str(valor_total)

    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {Tiempo} meses es: {valor_total}" 
    
    plantilla = "Para el usuario {usu} La cantidad de dinero a recibir, según el monto inicial {cant} para un tiempo de {Tiem} meses es: {valor_t}"
    return plantilla.format(usu= usuario, cant = cantidad , Tiem = Tiempo , valor_t = valor_total)

    """
    plantilla = "Para el usuario %s La cantidad de dinero a recibir, según el monto inicial %d para un tiempo de %d meses es: %.1f"
    return plantilla % (usuario, cantidad, Tiempo, valor_total)


print(CDT("ER3366" , 1000000 , 3))