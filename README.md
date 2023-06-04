# Proyecto de CRUD de Películas - FastAPI

<img src="img/programate-academy.png" alt="Logo Programate">

![Logo](https://www.python.org/static/community_logos/python-logo-inkscape.svg)

## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de un sistema de inventario. Está diseñado con un enfoque académico para que los aprendices de programación backend puedan utilizarlo como punto de partida y comenzar a trabajar sobre él.

## Funcionalidades

- Obtener toda la informacion sobre el sistema de inventario
- Obtener los productos por su ID
- Crear nuevos datos
- Actualizar datos existentes
- Eliminar datos

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/TheLostHeaven/Inventory_System


2. Navega al directorio del proyecto:

cd Inventory_System

3. Tienes que cambiar el origen del repositorio

git remote -v

git remote remove origin

git remote add origin <nueva_url_del_repositorio>

4. Instala las dependencias necesarias:

pip install -r requirements.txt


## Uso

1. Inicia la aplicación:

uvicorn main:app --reload


2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/docs


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD en el sistema de inventario.


## Contacto

Si tienes alguna pregunta o sugerencia o quieres el workbook para desarrollar este proyecto, no dudes en contactarme en [tiquedaniel2002@gmail.com](tiquedaniel2002@gmail.com).


## Autors

- [@Daniel Molina](https://github.com/TheLostHeaven)