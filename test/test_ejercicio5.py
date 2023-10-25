
import pytest
from src.ejercicio5 import *

class TestComprobarcontraseña:


    # Test de la función.
    def test_comprobarContraseña(self):
        
        assert comprobarContraseña("PepitoGrillo") == "PepitoGrillo"

    # Test contraseña incorrecta.
    def test_comprobarConstraseñaIncorrecta(self):
        password = "password"
        with pytest.raises(NameError):
            comprobarContraseña(password)

    # Test cadena vacía.
    def test_comprobarContraseñaStringVacio(self):
        password = ""
        with pytest.raises(NameError):
            comprobarContraseña(password)

    # Test de caracter.
    def test_comprobarContraseñaCaracter(self):
        password = "a"
        with pytest.raises(NameError):
            comprobarContraseña(password)

    # Test de texto largo.
    def test_comprobarContraseñaStringLargo(self):
        password = "a" * 100
        with pytest.raises(NameError):
            comprobarContraseña(password)

    # Test de texto en blanco.
    def test_comprobarContraseñaEnBlanco(self):
        password = "   "
        with pytest.raises(NameError):
            comprobarContraseña(password)