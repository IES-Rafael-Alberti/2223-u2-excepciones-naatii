import pytest
from src.ejercicio2 import *

class TestListaimpares:

    # Devuelve una lista con los impares 
    def test_listaImpares(self):
        assert listaImpares(5) == [1, 3, 5]

    # Devuelve 1 si se le pasa 1
    def test_listaImparesConUno(self):
        assert listaImpares(1) == [1]

    # Lanza un error si se le pasa un string
    def test_listaImparesErrorNegativo(self):
        with pytest.raises(ValueError):
            listaImpares(-12)
            

class TestParoimpar:

    @pytest.mark.parametrize(
            "numero , expected",
            [
                (2, True),
                (4, True),
                (6, True),
                (9223372036854775806, True),
                (1, False),
                (3, False),
                (5, False),
                (9223372036854775807, False),
            ]
    )
    # Devulución del uso de la función
    def test_parOImpar(self,numero,expected):
        assert parOImpar(numero) == expected
    # Devolución de error cuando se le pasa un string
    def test_parOImparErrorString(self):
        with pytest.raises(ValueError):
            parOImpar("a")