import pytest
from src.ejercicio4 import *

class TestComprobarnumero:

    @pytest.mark.parametrize(
            "numero, expected",
            [
                (5, 5),
                (0, 0),
                (-5, -5)
            ]
    )
    # Comprobar que la función funciona.
    def test_comprobarNumero(self, numero, expected):
        assert comprobarNumero(numero) == expected

    # Test para tipos de datos strings
    def test_comprobarNumeroErrorString(self):
        with pytest.raises(ValueError):
            comprobarNumero("a")

    # Test para tipos de datos floats
    def test_comprobarNumeroErrorFloat(self):
        with pytest.raises(ValueError):
            comprobarNumero(3.14)

    # Test para tipos de datos booleanos
    def test_comprobarNumeroErrorBoolean(self):
        with pytest.raises(ValueError):
            comprobarNumero(True)