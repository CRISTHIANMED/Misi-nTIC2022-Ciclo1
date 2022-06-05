def apto(Nombre, sexo , edad , estatura) -> str:
    """
    La oficina de incorporación del ejército necesita un algoritmo 
    que le pueda permitir saber si un aspirante a ingresar a la 
    institución como soldado es apto o no para poder vincularlo. 
    Para que una persona sea apta, debe cumplir los siguientes 
    requisitos:

    Si es mujer, su estatura debe ser superior a 1.60 mts y su 
    edad debe estar entre 20 y 25 años.

    Si el aspirante es hombre, se estatura debe ser superior a 
    1.65 mts y su edad debe estar entre los 18 y 24 años.

    Tanto mujeres como hombres deben ser solteros. Diseñe el 
    algoritmo de tal forma que permita informar si un aspirante 
    es apto o no para ingresar al ejercito.
    """
    if sexo == "f" or sexo == "F":
        if estatura >= 1.60:
            if edad >= 20 and edad <= 25:
                mensaje = "apto"
            else:
                mensaje = "no apto"
        else:
            mensaje = "no apto"
    elif sexo == "m" or sexo == "M":
        if estatura >= 1.65:
            if edad >= 18 and edad <= 24:
                mensaje = "apto"
            else:
                mensaje = "no apto"
        else:
             mensaje = "no apto"
    
    print(f"{Nombre} es {mensaje} para ingresar al ejercito")


apto("Cristhian", "M" , 23 , 1.75)