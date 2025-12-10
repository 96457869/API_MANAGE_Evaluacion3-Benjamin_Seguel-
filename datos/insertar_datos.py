from datos.conexion import Conexion
import mysql.connector

# --- FUNCIÓN QUE ESTABA FALTANDO ---
def insertar_nuevo_usuario(usuario):
    db = Conexion()
    conn = db.conectar()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
            # La contraseña ya viene encriptada desde el negocio
            valores = (usuario.username, usuario.password)
            cursor.execute(query, valores)
            conn.commit()
            print("Usuario registrado exitosamente en BD.")
            return True
        except mysql.connector.Error as err:
            print(f"Error al insertar usuario: {err}")
            return False
        finally:
            cursor.close()
            db.cerrar()
    return False

# --- FUNCIÓN PARA POSTS ---
def insertar_post(post):
    db = Conexion()
    conn = db.conectar()
    if conn:
        try:
            cursor = conn.cursor()
            # INSERT IGNORE evita errores si el ID ya existe
            query = "INSERT IGNORE INTO posts (id, userId, title, body) VALUES (%s, %s, %s, %s)"
            valores = (post.id, post.userId, post.title, post.body)
            cursor.execute(query, valores)
            conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error BD al insertar post: {err}")
            return False
        finally:
            cursor.close()
            db.cerrar()
    return False