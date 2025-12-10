from datos.conexion import Conexion
from modelos.modelos import Usuario, Post
import mysql.connector

def obtener_usuario_por_username(username):
    """
    Busca un usuario en la BD por su nombre de usuario.
    Retorna un objeto Usuario con su hash de contraseña.
    """
    db = Conexion()
    conn = db.conectar()
    usuario_obj = None
    
    if conn:
        try:
            # dictionary=True es vital para acceder por nombre de columna
            cursor = conn.cursor(dictionary=True)
            query = "SELECT * FROM usuarios WHERE username = %s"
            cursor.execute(query, (username,))
            row = cursor.fetchone()
            
            if row:
                # Si encontramos al usuario, creamos el objeto para devolverlo
                usuario_obj = Usuario(row['username'], row['password'], row['id'])
                
        except mysql.connector.Error as err:
            print(f"Error al obtener usuario: {err}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                db.cerrar()
            
    return usuario_obj

def obtener_todos_posts():
    """
    Recupera todos los posts guardados en la tabla 'posts'.
    """
    db = Conexion()
    conn = db.conectar()
    lista_posts = []
    
    if conn:
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM posts")
            resultados = cursor.fetchall()
            
            for row in resultados:
                # Reconstruimos objetos Post
                post = Post(row['userId'], row['id'], row['title'], row['body'])
                lista_posts.append(post)
                
        except mysql.connector.Error as err:
            print(f"Error leyendo posts: {err}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                db.cerrar()
    return lista_posts