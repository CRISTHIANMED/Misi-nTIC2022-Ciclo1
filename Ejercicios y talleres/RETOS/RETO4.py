from functools import reduce
def ordenes(rutinaContable):

    compra_minima = 600000
    incremento = 25000

    suma_total1 = list(map(lambda x: [x[0]] + list((map(lambda y : y[1]*y[2], x[1:]))), rutinaContable))

    suma_total2 = list(map(lambda x: [x[0]] + [reduce(lambda a, b : round(a + b, 2), x[1:])], suma_total1))

    suma_total3 = list(map(lambda x: x if x[1] >= compra_minima else [x[0] , x[1] + incremento], suma_total2))

    print('------------------------ Inicio Registro diario ---------------------------------')
    for lista_factura in suma_total3:
        mensaje = f"La factura {lista_factura[0]} tiene un total en pesos de {lista_factura[1]:,.2f}"
        print(mensaje)
    print('-------------------------- Fin Registro diario ----------------------------------')



rutinacontable = [
    [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
    [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
    [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
    [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]
ordenes(rutinacontable)

rutinacontable = [
    [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
    [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)] 
]

rutinacontable = [
    [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
    [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
    [6591, ("7812", 2, 11.99), ("9652",11,18.99)]
]