
from validador import verificar_de_acceso
def ejecutar_autenticacion():
    try:
        usuario_ingresado = input("ingrese su nombre de usuario: ")
        clave_ingresada = input("ingrese su contraseña: ")
        if verificar_acceso(usuario_ingresado, clave_ingresada):
            print("aceso concedido")
        else:
            print("credenciales incorrectas")
    except KeyboardInterrupt:
        print("\nEjecución cancelada por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante el flujo: {e}")
if __name__ == "__main__":
    ejecutar_autenticacion()
