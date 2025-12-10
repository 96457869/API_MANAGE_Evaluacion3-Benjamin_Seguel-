from servicios.peticiones import obtener_posts_api
from modelos.modelos import Post
from datos.insertar_datos import insertar_post
from datos.obtener_datos import obtener_todos_posts

def sincronizar_posts():
    """
    1. Llama a la API para traer los posts.
    2. Convierte los datos JSON en objetos Post.
    3. Guarda cada post en la base de datos local.
    """
    print("--- Iniciando Sincronización ---")
    print("Conectando a JSONPlaceholder...")
    
    # 1. Traer datos de internet
    datos_json = obtener_posts_api()
    
    if not datos_json:
        print("No se recibieron datos de la API (o hubo error de conexión).")
        return

    print(f"Se obtuvieron {len(datos_json)} posts de la API. Guardando en BD...")
    
    contador = 0
    # 2. Recorrer y guardar
    for item in datos_json:
        # Convertimos diccionario a Objeto
        nuevo_post = Post.desde_json(item)
        
        # Guardamos en SQL
        if insertar_post(nuevo_post):
            contador += 1
            
    print(f"¡Listo! Se han procesado {contador} posts en la base de datos local.")

def listar_posts_locales():
    """
    Consulta la base de datos local y muestra los posts en pantalla.
    """
    print("\n--- Listado de Posts en Base de Datos Local ---")
    posts = obtener_todos_posts()
    
    if not posts:
        print("La base de datos está vacía. Prueba la opción 'Sincronizar' primero.")
    else:
        # Mostramos solo los primeros 5 para no llenar la consola, o todos si prefieres
        print(f"Total encontrados: {len(posts)}")
        for i, p in enumerate(posts):
            print(f"[{p.id}] {p.title}")
            # Limite visual para que no sea eterno en la consola
            if i >= 9: 
                print("... (y muchos más) ...")
                break