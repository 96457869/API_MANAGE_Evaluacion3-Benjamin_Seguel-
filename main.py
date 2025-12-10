import sys
from negocio.negocio_users import registrar_usuario_logica, login_usuario_logica
from negocio.negocio_posts import sincronizar_posts, listar_posts_locales
from servicios.peticiones import enviar_post_api, actualizar_post_api, eliminar_post_api
# Importamos las validaciones nuevas
from auxiliares.validaciones import validar_no_vacio, validar_id, validar_longitud_password

def menu_principal():
    usuario_actual = None
    
    while True:
        print("\n=== SISTEMA DE GESTIÓN API_MANAGE ===")
        
        if not usuario_actual:
            print("1. Registrar Usuario")
            print("2. Iniciar Sesión")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                u = input("Ingrese nuevo usuario: ")
                p = input("Ingrese contraseña: ")
                
                # Usamos las validaciones aquí
                if validar_no_vacio(u) and validar_longitud_password(p):
                    if registrar_usuario_logica(u, p):
                        print("¡Registro exitoso! Ahora puede iniciar sesión.")
                    else:
                        print("Error: No se pudo registrar (quizás el usuario ya existe).")
            
            elif opcion == "2":
                u = input("Usuario: ")
                p = input("Contraseña: ")
                if validar_no_vacio(u) and validar_no_vacio(p):
                    usuario_actual = login_usuario_logica(u, p)
                    if usuario_actual:
                        print(f"\n¡Bienvenido al sistema, {usuario_actual.username}!")
            
            elif opcion == "0":
                print("Saliendo...")
                sys.exit()
            else:
                print("Opción no válida.")
        
        else:
            # Menú de Usuario Logueado
            print(f"\n--- Panel de Usuario: {usuario_actual.username} ---")
            print("1. Sincronizar Posts (API -> BD)")
            print("2. Ver Posts Locales")
            print("3. Enviar Post (POST)")
            print("4. Actualizar Post (PUT)")
            print("5. Eliminar Post (DELETE)")
            print("6. Cerrar Sesión")
            print("0. Salir")
            
            opcion = input("Seleccione una acción: ")

            if opcion == "1":
                sincronizar_posts()

            elif opcion == "2":
                listar_posts_locales()

            elif opcion == "3":
                titulo = input("Título: ")
                cuerpo = input("Cuerpo: ")
                if validar_no_vacio(titulo) and validar_no_vacio(cuerpo):
                    data = {"title": titulo, "body": cuerpo, "userId": usuario_actual.id}
                    enviar_post_api(data)

            elif opcion == "4":
                id_txt = input("ID del post a actualizar: ")
                id_valido = validar_id(id_txt)
                if id_valido:
                    titulo = input("Nuevo título: ")
                    if validar_no_vacio(titulo):
                        data = {"id": id_valido, "title": titulo, "body": "Update", "userId": usuario_actual.id}
                        actualizar_post_api(id_valido, data)

            elif opcion == "5":
                id_txt = input("ID del post a eliminar: ")
                id_valido = validar_id(id_txt)
                if id_valido:
                    eliminar_post_api(id_valido)

            elif opcion == "6":
                usuario_actual = None
                print("Sesión cerrada.")

            elif opcion == "0":
                sys.exit()
            else:
                print("Opción inválida.")

if __name__ == "__main__":
    menu_principal()