def AutoPartes (ventas: list) -> dict:
    dic_ventas = {}
    for tupla in ventas :
        if dic_ventas.get(tupla[0]):
            dic_ventas[tupla[0]].append(tupla)
        else:
            dic_ventas[tupla[0]] = []
            dic_ventas[tupla[0]].append(tupla)
    return (dic_ventas)

def consultaRegistro(ventas, idProducto):

    if ventas.get(idProducto):
        for producto in ventas.get(idProducto):
            print ("Producto consultado : {idProducto}  Descripción  {dProducto}  #Parte  {pnProducto}  Cantidad vendida  {cvProducto}  Stock  {sProducto}  Comprador {nComprador}  Documento  {cComprador}  Fecha Venta  {fVenta}".
                    format(idProducto=producto[0],dProducto=producto[1],pnProducto=producto[2],cvProducto=producto[3],sProducto=producto[4],nComprador=producto[5],cComprador=producto[6],fVenta=producto[7]))
    else: 
        print("No hay registro de venta de ese producto")



consultaRegistro(
    AutoPartes(
        [ 
          (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
          (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
          (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
          (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
          (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')
        ]
    ), 2010
)













    












"""
consultaRegistro(AutoPartes([
 ...(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
 ...(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
 ...(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
 ...(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
 ...(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)
"""