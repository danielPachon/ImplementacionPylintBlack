
# ImplementacionPylintBlack

## Descripción del Proyecto
**ImplementacionPylintBlack** es un proyecto diseñado para gestionar artículos y autores a través de una API. La implementación se lleva a cabo utilizando FastAPI, garantizando un alto rendimiento y eficiencia. Este proyecto utiliza Docker para facilitar la configuración de la base de datos y Adminer para la gestión visual. Además, se aseguran prácticas de codificación de calidad siguiendo las convenciones PEP8 con herramientas como Pylint y Black.

## Características Principales
- **Gestión de Artículos y Autores:** CRUD completo para las entidades de artículos y autores.
- **Seguridad Mejorada:** Acceso a la API protegido mediante una clave API.
- **Estructura Modular:** Código organizado en diferentes carpetas para facilitar la mantenibilidad y escalabilidad.
- **Dockerización:** Facilita la configuración del entorno y la ejecución de la aplicación.

## Instalación y Configuración
1. **Variables de Entorno**
   Se incluye un archivo `.env_example` que contiene las variables de entorno necesarias. Debes crear un archivo `.env` en el directorio raíz del proyecto y configurar tus propias variables:
   ```bash
   cp .env.example .env
   ```
   Luego, edita el archivo `.env` con los valores correctos para tu entorno:
   ```dotenv
   API_KEY=tu_api_key
   MYSQL_ROOT_PASSWORD=ejemplo
   MYSQL_DATABASE=db_ejemplo
   MYSQL_HOST=ejemplo
   MYSQL_PORT=3306
   MYSQL_USER=ejemplo
   MYSQL_PASSWORD=ejemplo
   ```

2. **Construcción y Ejecución con Docker**
   El proyecto incluye un archivo Makefile para facilitar la ejecución de los servicios. Simplemente ejecuta el siguiente comando para iniciar los contenedores:
   ```bash
   make deploy
   ```
   **Nota:** Si estás en Windows, utiliza estos comandos en su lugar:
   ```bash
   docker compose build
   docker compose up -d
   ```

3. **Acceso a Adminer**
   Adminer está disponible en [http://localhost:8080](http://localhost:8080) para la gestión visual de la base de datos. Los detalles de conexión son definidos en el archivo `docker-compose.yml`.

4. **Configuración de Pylint**
   Para analizar la calidad del código, ejecuta:
   ```bash
   pylint nombre_del_paquete.py
   ```
   Puedes personalizar las reglas de Pylint en el archivo `.pylintrc`.

5. **Formateo de Código con Black**
   Para formatear el código siguiendo las convenciones PEP8, utiliza:
   ```bash
   black nombre_del_paquete.py
   ```
   O para formatear todo el proyecto:
   ```bash
   black .
   ```

## Estructura del Proyecto
```
ImplementacionPylintBlack/
├── FastAPI/
│   ├── app/
│   │   ├── config/                # Configuración de la base de datos y variables de entorno
│   │   │   └── database.py
│   │   ├── routes/                # Definiciones de las rutas API
│   │   │   ├── article_route.py    # Rutas para gestionar artículos
│   │   │   └── author_route.py     # Rutas para gestionar autores
│   │   ├── schemas/               # Esquemas de datos para la API
│   │   │   ├── article.py          # Esquema para el artículo
│   │   │   └── author.py           # Esquema para el autor
│   │   ├── services/              # Lógica de negocio y servicios de la API
│   │   │   ├── article_service.py   # Servicios relacionados con artículos
│   │   │   └── author_service.py    # Servicios relacionados con autores
│   │   └── main.py                # Punto de entrada para la aplicación FastAPI
├── Dockerfile                      # Dockerfile para el backend de FastAPI
├── requirements.txt                # Dependencias de Python
├── MySQL/                          # Configuración y volúmenes de MySQL
│   └── Dockerfile                  # Dockerfile para la base de datos MySQL
├── docker-compose.yml              # Configuración de Docker Compose
├── Makefile                        # Script para facilitar la ejecución de contenedores
├── .env_example                    # Archivo de ejemplo de variables de entorno
└── .pylintrc                       # Configuración de Pylint
```

## Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor abre un issue o crea un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
