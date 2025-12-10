class Usuario:
    def __init__(self, username, password, id=None):
        self.id = id
        self.username = username
        self.password = password

    # Método para mostrar el objeto como texto (útil para debug)
    def __str__(self):
        return f"Usuario(id={self.id}, username={self.username})"

class Post:
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

    # Esto cumple con el requisito de "Deserializar" (Convertir JSON a Objeto)
    @classmethod
    def desde_json(cls, data):
        return cls(
            userId=data.get('userId'),
            id=data.get('id'),
            title=data.get('title'),
            body=data.get('body')
        )

    def __str__(self):
        return f"Post {self.id}: {self.title}"