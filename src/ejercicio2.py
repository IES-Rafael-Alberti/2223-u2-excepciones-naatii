ERROR001 = "ERROR 001: Debe introducir un número, además debe ser positivo."

def parOImpar(numero:int)->bool:
    if type(numero) == int:
        if numero % 2 == 0:
            return True
        else:
            return False
    else:
        raise ValueError()
        
def listaImpares(numero:int)->list:
    impares =  []
    if numero > 0:
        for i in range(1, numero + 1):
            if not parOImpar(i):
                impares.append(i)
        return impares
    else:
        raise ValueError()

if __name__=="__main__":
    try:
        numero = int(input("Introduce un número: "))
        print(listaImpares(numero))
    except ValueError:
        print(ValueError(ERROR001))