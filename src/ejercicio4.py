ERROR001 = "ERROR 001: Por favor introduce un número"
def comprobarNumero(numero:int)->int:
    """Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.

    Args:
        cuentaAtras (int): El número del usuario para comprobar si es número o no.

    Returns:
        int: Devuelve el número si es correcto.
    """
    if type(numero) == int:
        return numero
    else:
        raise ValueError(ERROR001)

if __name__ == "__main__":
    numeroCorrecto = False
    while not numeroCorrecto:
        try:
            numero = int(input("Escribe un número: "))
            numeroCorrecto = True
        except:
            print("introduce un número correcto") if not numeroCorrecto else print("El número es correcto")

    print(comprobarNumero(numero))