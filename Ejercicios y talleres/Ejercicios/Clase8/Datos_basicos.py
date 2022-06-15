datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"26938401",
    "fecha_nacimiento":"03/12/1980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela", 
    "nacionalidad":"Venezolana",
    "estado_civil":"Soltero"
}

for clave, valor in datos_basicos.items(): 
    print(f"{clave:17}: {valor}")