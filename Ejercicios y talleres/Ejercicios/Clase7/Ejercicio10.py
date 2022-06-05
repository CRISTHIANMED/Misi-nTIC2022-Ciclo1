def LA(año):
    if int(año) >= 2000:
        A = 2*(20-int(año[0:2]))
    else:
        A = 2*(19-int(año[0:2]))+1
    return A

def LB(año):
    B = int(año[2:4]) + (int(año[2:4])//4)
    return B

def LC(año,mes):
    if bisiesto(año) == True:
        if mes == "01" or mes == "02":
            C = -1
        else:
            C = 0
    else:
        C = 0
    
    return C

def LD(mes):
    if mes == "01": D = 6
    elif mes == "02": D = 2
    elif mes == "03": D = 2
    elif mes == "04": D = 5
    elif mes == "05": D = 0
    elif mes == "06": D = 3
    elif mes == "07": D = 5
    elif mes == "08": D = 1
    elif mes == "09": D = 4
    elif mes == "10": D = 6
    elif mes == "11": D = 2
    elif mes == "12": D = 4

    return D

def bisiesto(año):
    if año[2:4] == "00":
        if (int(año) % 400) == 0:
            bis = True
        else:
            bis = False
    else:
        if (int(año[2:4]) % 4) == 0:
            bis = True
        else:
            bis = False
    
    return bis

def Ldia(R):
    if R == 1: dia = "Lunes" 
    elif R == 2: dia = "Martes" 
    elif R == 3: dia = "Miércoles"
    elif R == 4: dia = "Jueves"
    elif R == 5: dia = "Viernes"
    elif R == 6: dia = "Sábado"
    elif R == 0: dia = "Domingo"

    return dia

def dia_fecha (fecha):

    """
    Escribir un programa que pregunte al usuario la fecha de su 
    nacimiento en formato 'dd/mm/aaaa' y calcule el dia de la 
    semana que nació.
    """
    L_fecha = fecha.split("/")

    dia = L_fecha[0]
    mes = L_fecha[1]
    año = L_fecha[2]

    A = LA(año) 
    B = LB(año)
    C = LC(año,mes) 
    D = LD(mes)
    E = int(dia)

    S = A + B + C + D + E
    R = S % 7

    DIA = Ldia(R)

    return DIA

print("Su dia de nacimiento es: " , dia_fecha("17/02/2222"))