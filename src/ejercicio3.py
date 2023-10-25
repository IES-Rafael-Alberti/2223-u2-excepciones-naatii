ERROR001 = "ERROR 001: Por favor introduce un número"
def cuentaAtras(numero:int)->list:
    """Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

    Args:
        cuentaAtras (int): El número del usuario para realizar la cuenta atrás.

    Returns:
        list: la lista de todos número de la cuentra atrás
    """
    numeros = []
    if numero>0:
        for numero in range(numero, -1, -1): numeros.append(numero)
        return numeros
    else:
        raise ValueError(ERROR001)

if __name__ == "__main__":
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            edadInput = int(input("Escribe un número: "))
            numeroCorrecto = True
        except:
            if not numeroCorrecto:
                print("introduce un número correcto")
            else:
                print("El número es correcto")

    print(cuentaAtras(edadInput))