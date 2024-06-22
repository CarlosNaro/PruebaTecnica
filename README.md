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
2. Crea un entorno virtual con `python -m venv env`.
3. Activa el entorno virtual con `env\Scripts\activate` (en Windows) o `source env/bin/activate` (en Unix o MacOS).
4. Instala las dependencias con `pip install -r requirements.txt`.
5. Ejecuta las migraciones con `python manage.py migrate`.
6. Inicia el servidor con `python manage.py runserver`.

## Cómo Usar

1. Clona el repositorio y sigue las instrucciones de instalación.
2. Navega a `http://localhost:8000/admin` en tu navegador para acceder al panel de administración de Django.
3. Inicia sesión con tu superusuario. Si aún no has creado un superusuario, puedes hacerlo
   ejecutando `python manage.py createsuperuser` en tu terminal y siguiendo las instrucciones.
4. En el panel de administración, ve a 'Usuarios' y haz clic en 'Añadir usuario' para crear un nuevo usuario.
5. Una vez que hayas creado un usuario, puedes cerrar sesión del panel de administración.
6. Navega a `http://localhost:8000` en tu navegador e inicia sesión con las credenciales del usuario que acabas de
   crear.
7. Utiliza el formulario para cargar un archivo de contratos de alquiler.
8. Utiliza el campo de búsqueda para buscar contratos.
9. Selecciona las columnas que deseas exportar a Excel y haz clic en "Exportar a Excel".