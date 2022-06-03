def descuento (valor_boleta:int , descuento:int , primer_ingreso:bool) -> int:
    if primer_ingreso== True:
            total_boleta = valor_boleta*(1-(descuento/100))
    else:
            total_boleta = valor_boleta
    return total_boleta


def cliente (informacion:dict) -> dict:

    if informacion["edad"] > 18 :
        total_boleta = descuento (20000, 5, informacion["primer_ingreso"])
        Atraccion = "X-Treme"
        Apto = True
    elif informacion["edad"] >= 15 and informacion["edad"] <= 18:
        total_boleta = descuento (5000, 7, informacion["primer_ingreso"])
        Atraccion = "Carros chocones"
        Apto = True
    elif informacion["edad"] >= 7 and informacion["edad"] < 15 :
        total_boleta = descuento (10000, 5, informacion["primer_ingreso"])
        Atraccion = "Sillas voladoras"
        Apto = True
    else:
        total_boleta ="N/A"
        Atraccion = "N/A"
        Apto = False
    
    cliente = {
        "nombre": informacion["nombre"],
        "edad": informacion["edad"],
        "atraccion": Atraccion,
        "apto": Apto,
        "primer_ingreso": informacion["primer_ingreso"],
        "total_boleta": total_boleta    
    }

    return cliente


informacion = {
    "id_cliente": 1,
    "nombre": "Johana Fernandez",
    "edad": 8,
    "primer_ingreso": False
}

print(cliente(informacion))