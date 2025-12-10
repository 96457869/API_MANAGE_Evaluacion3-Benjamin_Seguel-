import bcrypt
from datos.insertar_datos import insertar_nuevo_usuario
from datos.obtener_datos import obtener_usuario_por_username
from modelos.modelos import Usuario

def encriptar_password(password):
    """
    Convierte una contraseña de texto plano en un hash seguro.
    """
    # bcrypt requiere bytes
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def validar_password(password_plano, password_hashed):
    """
    Compara la contraseña ingresada con el hash guardado en la BD.
    """
    if isinstance(password_hashed, str):
        password_hashed = password_hashed.encode('utf-8')
    
    return bcrypt.checkpw(password_plano.encode('utf-8'), password_hashed)

def registrar_usuario_logica(username, password):
    """
    Lógica para registrar: encripta la clave y llama a la capa de datos.
    """
    try:
        if not username or not password:
            print("Error: Usuario y contraseña son obligatorios.")
            return False

        # 1. Encriptamos la contraseña
        password_segura = encriptar_password(password)

        # 2. Creamos el objeto Usuario
        nuevo_usuario = Usuario(username, password_segura)

        # 3. Lo mandamos a guardar a la BD
        return insertar_nuevo_usuario(nuevo_usuario)
    except Exception as e:
        print(f"Error en lógica de registro: {e}")
        return False

def login_usuario_logica(username, password):
    """
    Lógica de Login: Busca usuario y verifica la contraseña encriptada.
    """
    usuario_encontrado = obtener_usuario_por_username(username)
    
    if usuario_encontrado:
        if validar_password(password, usuario_encontrado.password):
            return usuario_encontrado
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")
    
    return None