def diferencia(capacidad_vaso,capacidad_actual):
    dif_cap=capacidad_vaso-capacidad_actual
    return dif_cap

def ordenar(amigo_1:dict, amigo_2:dict, amigo_3:dict):
    dif1 = diferencia(amigo_1["capacidad_vaso"],amigo_1["capacidad_actual"])
    dif2 = diferencia(amigo_2["capacidad_vaso"],amigo_2["capacidad_actual"])
    dif3 = diferencia(amigo_3["capacidad_vaso"],amigo_3["capacidad_actual"])

    orden = {}
    if dif1 <= dif2 and dif2 <= dif3:
        orden["primero"] = amigo_1
        orden["segundo"] = amigo_2
        orden["tercero"] = amigo_3
    elif dif1 <= dif3 and dif3 <= dif2:
        orden["primero"] = amigo_1
        orden["segundo"] = amigo_3
        orden["tercero"] = amigo_2
    elif dif2 <= dif1 and dif1 <= dif3:
        orden["primero"] = amigo_2
        orden["segundo"] = amigo_1
        orden["tercero"] = amigo_3
    elif dif2 <= dif3 and dif3 <= dif1:
        orden["primero"] = amigo_2
        orden["segundo"] = amigo_3
        orden["tercero"] = amigo_1
    elif dif3 <= dif1 and dif1 <= dif2:
        orden["primero"] = amigo_3
        orden["segundo"] = amigo_1
        orden["tercero"] = amigo_2
    elif dif3 <= dif2 and dif2 <= dif1:
        orden["primero"] = amigo_3
        orden["segundo"] = amigo_2
        orden["tercero"] = amigo_1
    
    return orden
    

def desperdicio_de_gaseosa(amigo_1:dict, amigo_2:dict, amigo_3:dict, capacidad_boton:float)->str:
    
    orden = ordenar(amigo_1, amigo_2 , amigo_3)
    dif1 = diferencia(orden["primero"]["capacidad_vaso"],orden["primero"]["capacidad_actual"])
    dif2 = diferencia(orden["segundo"]["capacidad_vaso"],orden["segundo"]["capacidad_actual"])
    dif3 = diferencia(orden["tercero"]["capacidad_vaso"],orden["tercero"]["capacidad_actual"])

    if dif1//capacidad_boton == 0 or dif2//capacidad_boton == 0 or dif3//capacidad_boton == 0:  
        
        primero = orden["primero"]["nombre"]
        segundo = orden["segundo"]["nombre"]
        tercero = orden["tercero"]["nombre"]

        mensaje = f"Primero llena a {primero}, luego a {segundo}, luedo a {tercero}"

    else:

        mensaje = "None"

    return mensaje


amigo_1 = {
    "nombre" : "Cristhian",
    "capacidad_vaso" : 5.5,
    "capacidad_actual" : 2.5
}

amigo_2 = {
    "nombre" : "Esteban",
    "capacidad_vaso" : 4,
    "capacidad_actual" : 2.5
}

amigo_3 = {
    "nombre" : "Daniel",
    "capacidad_vaso" : 5.5,
    "capacidad_actual" : 2.5
}

capacidad_boton = 1.6

print(desperdicio_de_gaseosa(amigo_1, amigo_2, amigo_3, capacidad_boton))
