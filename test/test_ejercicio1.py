import pytest
from src.ejercicio1 import *

@pytest.mark.parametrize(
    "edad, expected",
    [
        (2, [1,2]),
        (5, [1,2,3,4,5]),
        (7, [1,2,3,4,5,6,7])
    ]
)
def test_calcularAños(edad, expected):
    assert calcularAños(edad) == expected

def test_calculaAñosError():
    with pytest.raises(ValueError):
        calcularAños("asd")