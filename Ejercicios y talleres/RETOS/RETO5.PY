import pandas as pd

rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true'

def listaPeliculas(rutaFileCsv: str) -> str:

    try:
        extension = rutaFileCsv.split('.')[-1]
        if "csv" in extension:
            archivo = pd.read_csv(rutaFileCsv)
            archivo1 = archivo[["Country","Language","Gross Earnings"]]
            archivo2 = archivo1.pivot_table(index=['Country', 'Language'])
            resp = archivo2.head(10)
        else:
            error = 'Extensión inválida.'
            resp = error
        return resp
    except:
        return 'Error al leer el archivo de datos.'
            

print(listaPeliculas(rutaFileCsv))








 







        


