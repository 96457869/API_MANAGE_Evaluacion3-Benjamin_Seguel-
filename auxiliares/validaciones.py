def validar_no_vacio(texto):
    """Retorna True si el texto tiene contenido, False si está vacío."""
    if texto and texto.strip():
        return True
    print("Error: El campo no puede estar vacío.")
    return False

def validar_id(valor):
    """Intenta convertir el valor a número entero. Retorna el ID o None."""
    try:
        id_num = int(valor)
        if id_num > 0:
            return id_num
        else:
            print("Error: El ID debe ser un número positivo.")
            return None
    except ValueError:
        print("Error: Debe ingresar un número válido.")
        return None

def validar_longitud_password(password, min_length=4):
    """Verifica que la contraseña tenga un largo mínimo."""
    if len(password) >= min_length:
        return True
    print(f"Error: La contraseña debe tener al menos {min_length} caracteres.")
    return False