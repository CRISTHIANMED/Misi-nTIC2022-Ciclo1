from math import factorial, pi

def Ejercicio_1(nombre:str):
    """
    Generación de ¡Hola <nombre>!

    Parámetros
        nombre: Cadena con el nombre
    Retorna
        Impresion de ¡Hola <nombre>!
    """
    print ("¡Hola {}!".format(nombre) )

def Ejercicio_2(n:int) -> int :
    """
    Calculo de factorial

    Parámetros
        n: Numero positivo
    Retorna
        F: Factorial del numero dado
    """
    F=factorial(n)
    return F

def Ejercicio_3(cantidad:int, iva=19) -> float :
    """
    Calculo de una factura

    Parámetros
        Cantidad: La cantidad de la factura sin IVA
        IVA: Iva aplicar por defecto 19%
    Retorna
        Total: total de una factura tras aplicarle el IVA
    """

    Total = cantidad*(1+(iva/100))
    return Total

def vol_cil(r:float,h:float)->float:
    """
    Calculo de volumen de un cilindro

    Parámetros
        r: Radio del circulo de la base 
        h: Altura del cilindro
    Retorna
        volumen: Volumen de un cilindro
    """
    Volumen = area_cir(r)*h
    return Volumen 

def area_cir(r:float)->float:
    """
    Calculo de area de un circulo

    Parámetros
        r: Radio del circulo
    Retorna
        Area: Area del circulo
    """

    Area =  pi*r**2
    return Area

def Ejercicio_5():
    """
    Suma de los primeros enteros positivos hasta n

    Parámetros
        
    Retorna
        Imprime en pantalla la suma de todos los enteros desde 1 hasta n
    """
    n = input("Ingrese  entero positivo n : ")
    n = int(n)

    Suma = int((n*(n+1))/2)

    print("La suma de los enteros de 1 hasta {} es: {}".format(n, Suma))

def Ejercicio_6():

    """
    Calculo el índice de masa corporal 

    Parámetros
        Por el usuario masa y estatura
    Retorna
        Imprime en pantalla tu indice de masa corporal
    """
    m = input("Ingrese  su peso en Kg: ")
    h = input("Ingrese  su estatura en m: ")

    m = float(m)
    h = float(h)

    IMC= m/(h**2) 
    print("Tu indice de masa corporal es %.2f" % IMC)


def Ejercicio_7(N_payasos:int, N_muñecas:int) -> int:

    """
    Calcule el peso total del paquete que será enviado. 

    Parámetros
        N_payasos: nu,ero de payasos
        N_muñecas: numero de muñecas
    Retorna
        P_total: peso total del paquete que será enviado.
    """
    payasos = 112
    muñecas = 75

    P_total = N_payasos*payasos + N_muñecas*muñecas

    return P_total


def Ejercicio_10(seg:int):

    """
    Parámetros
        segundos: Tiempo a convertir en segundos
    Retorna
        Imprime el equivalente en dias, horas, minutos y segundos
    """
    dias = seg // (60*60*24)
    moddias = seg % (60*60*24)

    horas = moddias // (60*60)
    modhoras = moddias % (60*60)

    minutos = modhoras // 60
    modminutos = modhoras % 60
    
    segundos = modminutos 


    print("{} segundos serán {} dias, {} horas , {} minutos y {} segundos".format(seg,dias,horas,minutos,segundos))





























