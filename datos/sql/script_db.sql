CREATE DATABASE IF NOT EXISTS db_api_manage;
USE db_api_manage;

-- Tabla para usuarios (La contraseña será un hash largo)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Tabla para guardar los Posts que traigamos de la API
CREATE TABLE IF NOT EXISTS posts (
    id INT PRIMARY KEY, -- Usamos el ID original de la API
    userId INT,
    title VARCHAR(255),
    body TEXT
);


