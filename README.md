# 🏥 MediTurnos - Sistema de Gestión de Salud

[cite_start]**MediTurnos** es una solución tecnológica diseñada para optimizar la asignación de citas médicas y la administración de pacientes en centros de salud.

## 🛠️ Stack Tecnológico
* [cite_start]**Lenguaje:** Python 
* [cite_start]**Framework:** Django
* [cite_start]**Base de Datos:** PostgreSQL

## 🏗️ Arquitectura
[cite_start]El proyecto sigue una **Arquitectura en Capas**, separando las responsabilidades para garantizar mantenibilidad y seguridad de los datos:
1. [cite_start]**Capa de Presentación:** Interfaz de usuario y formularios.
2. [cite_start]**Capa de Negocio:** Lógica de validación de turnos y disponibilidad.
3. [cite_start]**Capa de Datos/Entidad:** Modelos de datos y persistencia en PostgreSQL.

## 🚀 Instalación
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno e instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar migraciones: `python manage.py migrate`.
