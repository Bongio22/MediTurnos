# 🏥 MediTurnos - Sistema de Gestión de Salud

[cite_start]**MediTurnos** es una solución tecnológica diseñada para optimizar la asignación de citas médicas y la administración de pacientes en centros de salud[cite: 501, 539].

## 🛠️ Stack Tecnológico
* [cite_start]**Lenguaje:** Python [cite: 441, 576]
* [cite_start]**Framework:** Django [cite: 582]
* [cite_start]**Base de Datos:** PostgreSQL [cite: 444, 446]

## 🏗️ Arquitectura
[cite_start]El proyecto sigue una **Arquitectura en Capas**, separando las responsabilidades para garantizar mantenibilidad y seguridad de los datos[cite: 517, 574, 575]:
1. [cite_start]**Capa de Presentación:** Interfaz de usuario y formularios[cite: 534, 553].
2. [cite_start]**Capa de Negocio:** Lógica de validación de turnos y disponibilidad[cite: 552, 555].
3. [cite_start]**Capa de Datos/Entidad:** Modelos de datos y persistencia en PostgreSQL[cite: 530, 531].

## 🚀 Instalación
1. Clonar el repositorio.
2. Crear entorno virtual: `python -m venv venv`.
3. Activar entorno e instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar migraciones: `python manage.py migrate`.
