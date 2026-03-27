# 🏥 MediTurnos - Sistema de Gestión de Salud

**MediTurnos** es una solución tecnológica diseñada para optimizar la asignación de citas médicas y la administración de pacientes en centros de salud.

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 
* **Framework:** Django
* **Base de Datos:** PostgreSQL

## 🏗️ Arquitectura
El proyecto sigue una **Arquitectura en Capas**, separando las responsabilidades para garantizar mantenibilidad y seguridad de los datos:
1. **Capa de Presentación:** Interfaz de usuario y formularios.
2. **Capa de Negocio:** Lógica de validación de turnos y disponibilidad.
3. **Capa de Datos/Entidad:** Modelos de datos y persistencia en PostgreSQL.

## 🚀 Instalación
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno e instalar dependencias: `.\venv\Scripts\activate`, `pip install django psycopg2-binary`, .
4. Ejecutar migraciones: `python manage.py migrate`.
