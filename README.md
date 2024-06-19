# Prueba Técnica - Alquiler de Autos

Este proyecto es una aplicación web para gestionar el alquiler de autos. Permite a los usuarios cargar contratos de
alquiler, buscar contratos y exportar los detalles de los contratos a Excel.

## Características

- Carga de contratos de alquiler a través de un formulario.
- Búsqueda de contratos de alquiler.
- Exportación de detalles de contratos a Excel.
- Paginación de resultados de búsqueda.

## Tecnologías Utilizadas

- Python
- Django
- Openpyxl para la generación de archivos Excel.
- HTML y JavaScript para la interfaz de usuario.
- PostgreSQL como base de datos.

## Cómo Instalar

1. Clona el repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Ejecuta las migraciones con `python manage.py migrate`.
4. Inicia el servidor con `python manage.py runserver`.

## Cómo Usar

1. Navega a `http://localhost:8000` en tu navegador.
2. Utiliza el formulario para cargar un archivo de contratos de alquiler.
3. Utiliza el campo de búsqueda para buscar contratos.
4. Selecciona las columnas que deseas exportar a Excel y haz clic en "Exportar a Excel".

