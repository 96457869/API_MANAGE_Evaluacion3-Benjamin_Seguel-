# 🚀 API MANAGER - BENJAMÍN SEGUEL
### 🎓 Evaluación Sumativa 3 - Programación Orientada a Objetos Segura

Este proyecto implementa un sistema modular en Python que consume una API externa (JSONPlaceholder), gestiona usuarios con seguridad criptográfica y persiste datos en MySQL.

---

## 📋 Características Principales

* **🔐 Seguridad:** Encriptación de contraseñas usando `Bcrypt` (Hashing seguro).
* **🌐 Consumo API:** Métodos GET, POST, PUT y DELETE integrados.
* **🗄️ Base de Datos:** Persistencia local de usuarios y posts en MySQL.
* **🏗️ Modularidad:** Estructura MVC separada en capas (Modelos, Negocio, Datos, Servicios).
* **✅ Validaciones:** Control de entradas vacías y formatos correctos.

---

## ⚙️ Requisitos de Instalación

1.  **Python 3.x** instalado.
2.  **Servidor MySQL** (XAMPP recomendado) en ejecución.
3.  Instalar librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Puesta en Marcha

1.  **Base de Datos:**
    * Abre tu gestor SQL (phpMyAdmin).
    * Importa o ejecuta el script ubicado en: `datos/sql/script_db.sql`.

2.  **Ejecutar el Sistema:**
    ```bash
    python main.py
    ```

---

## 📂 Estructura del Proyecto

```text
API_MANAGE/
├── 📁 auxiliares/       # Constantes y Validaciones
├── 📁 datos/            # Conexión MySQL y Scripts SQL
├── 📁 modelos/          # Clases (POO)
├── 📁 negocio/          # Lógica y Encriptación (Bcrypt)
├── 📁 servicios/        # Conexión HTTP (Requests)
├── 📄 main.py           # Menú Principal
├── 📄 requirements.txt  # Dependencias
└── 📄 README.md         # Documentación

Developed by Benjamin Seguel for TI3021.