ERROR001 = "ERROR 001: Debe introducir un número."
def calcularAños(edad:int)->list:
    """Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

    Raises:
        ValueError: Excepcion por si el usuario introduce un tipo de dato no válido.

    Returns:
        list: devuelve una lista con todos los años desde 1 hasta los años que tiene.
    """
    años = []
    if type(edad) == int:
        for año in range(1, edad + 1):
            años.append(año)
        return años
    else:
        raise ValueError()
if __name__=="__main__":
    try:
        print(calcularAños(int(input("introduce su edad: "))))
    except ValueError:
        print(ValueError(ERROR001))