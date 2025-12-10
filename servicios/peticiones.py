import requests
from auxiliares.api_data import URL_BASE

def obtener_posts_api():
    """
    Solicitud GET a la API para traer la lista de posts.
    """
    url = f"{URL_BASE}/posts"
    try:
        respuesta = requests.get(url)
        # Si la respuesta es exitosa (Código 200)
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            print(f"Error HTTP al obtener datos: {respuesta.status_code}")
            return []
    except Exception as e:
        print(f"Error de conexión: {e}")
        return []

def enviar_post_api(data_dict):
    """
    Simula el envío de un nuevo post (POST).
    """
    url = f"{URL_BASE}/posts"
    try:
        respuesta = requests.post(url, json=data_dict)
        if respuesta.status_code == 201: # 201 significa "Creado"
            print("¡Éxito! La API respondió que el recurso fue creado.")
            return respuesta.json()
        else:
            print(f"Error en POST: {respuesta.status_code}")
    except Exception as e:
        print(f"Error enviando datos: {e}")

def actualizar_post_api(id_post, data_dict):
    """
    Simula la actualización de un post (PUT).
    """
    url = f"{URL_BASE}/posts/{id_post}"
    try:
        respuesta = requests.put(url, json=data_dict)
        if respuesta.status_code == 200:
            print(f"Post {id_post} actualizado correctamente en la API.")
            return True
        print(f"Error en PUT: {respuesta.status_code}")
    except Exception as e:
        print(f"Error en PUT: {e}")
    return False

def eliminar_post_api(id_post):
    """
    Simula la eliminación de un post (DELETE).
    """
    url = f"{URL_BASE}/posts/{id_post}"
    try:
        respuesta = requests.delete(url)
        if respuesta.status_code == 200:
            print(f"Post {id_post} eliminado correctamente en la API.")
            return True
        print(f"Error en DELETE: {respuesta.status_code}")
    except Exception as e:
        print(f"Error en DELETE: {e}")
    return False