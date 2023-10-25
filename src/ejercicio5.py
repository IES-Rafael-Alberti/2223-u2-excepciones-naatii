ERROR002 = "ERROR 002: Incorrect password"
CONTRASEÑA = "PepitoGrillo"
def comprobarContraseña(contraseñaUsuario:str)->str:
    if contraseñaUsuario == CONTRASEÑA:
        return contraseñaUsuario
    else:
        raise NameError()

if __name__=="__main__":
    try:
        contraseñaUsuario = input("introduce una contraseña: ")
        print(comprobarContraseña(contraseñaUsuario))
    except NameError:
        print(NameError(ERROR002))