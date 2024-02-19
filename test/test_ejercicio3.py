import pytest
from src.ejercicio3 import *

class TestCuentaatras:

    @pytest.mark.parametrize(
            "numero, expected",
            [
                (5,[5, 4, 3, 2, 1, 0]),
                (10, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
                (1, [1, 0])
            ]
    )
    # Test de la función
    def test_cuentaAtras(self, numero, expected):
        assert cuentaAtras(numero) == expected

    # Test si se introduce un número negativo
    def test_cuentaAtrasErrorNegative(self):
        with pytest.raises(ValueError):
            cuentaAtras(-1)

    # TEst si se introduce un string
    def test_cuentaAtrasErrorString(self):
        with pytest.raises(TypeError):
            cuentaAtras("5")

    # Test si se introduce un tipo de dato no contemplado
    def test_cuentaAtrasErrorFloat(self):
        with pytest.raises(TypeError):
            cuentaAtras(5.5)