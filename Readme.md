<h1 align="center"> Social NetWork</h1>

<p align="center"><img src="static/img/logo.png"/></p> 

## Tabla de contenidos:
- [Descripción y contexto](#descripción-y-contexto)
- [Guía de usuario](#guía-de-usuario)
- [Guía de instalación](#guía-de-instalación)
- [Cómo contribuir](#cómo-contribuir)
- [Código de conducta](#código-de-conducta)
- [Autor/es](#autores)
- [Información adicional](#información-adicional)
- [Variables de Entorno](#variables-de-entorno)

## Descripción y contexto
¡Bienvenidos al proyecto Social NetWork con Django! En este proyecto, he desarrollado una plataforma de redes sociales robusta y dinámica utilizando el potente framework Django. Nuestra meta principal ha sido crear un espacio interactivo donde los usuarios puedan compartir sus pensamientos, interactuar con sus amigos y mantenerse conectados de manera efectiva.

## Guía de usuario
Explica los pasos básicos sobre cómo usar la herramienta digital. Es una buena sección para mostrar capturas de pantalla o gifs que ayuden a entender la herramienta digital.
 	
## Guía de instalación
### Requisitos previos:
- Python 3.x instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Pasos para la instalación:

1. **Crear un entorno virtual (opcional pero recomendado):**
   Es una buena práctica crear un entorno virtual para cada proyecto Python. Esto ayuda a mantener las dependencias del proyecto separadas de otros proyectos y del sistema global. Para crear un entorno virtual, abre una terminal y ejecuta los siguientes comandos:

   ```bash
    python -m venv myenv
   ```
    Esto creará un nuevo directorio llamado `myenv` que contendrá el entorno virtual.

2. **Activar el entorno virtual:**
    ```bash
       .\env\Scripts\activate
    ```
    Esto activará el entorno virtual. Verás `(myenv)` en el prefijo de tu línea de comandos, lo que indica que el entorno virtual está activo.

3. **Instalar las librerías requeridas:**
    ```bash
    pip install requirements
    ```
    Este comando instalará todas las librerías especificadas en la versión exacta indicada.

4. **Desactivar el entorno virtual (opcional):**
Cuando hayas terminado de trabajar en tu proyecto, puedes desactivar el entorno virtual con el siguiente comando:
    ```bash
    deactivate
    ```

### Dependencias
#### Librerías y Frameworks:

- **Django**
  - Descripción: Framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y limpio.
  - Última versión probada: 5.0.2
  - Licencia: Licencia BSD

- **asgiref**
  - Descripción: Biblioteca de compatibilidad para trabajar con diferentes servidores web y aplicaciones ASGI.
  - Última versión probada: 3.7.2
  - Licencia: Licencia BSD

- **certifi**
  - Descripción: Paquete que contiene certificados raíz de confianza.
  - Última versión probada: 2024.2.2
  - Licencia: Licencia MPL-2.0

- **charset-normalizer**
  - Descripción: Biblioteca Python para normalizar nombres de caracteres.
  - Última versión probada: 3.3.2
  - Licencia: Licencia MIT

- **idna**
  - Descripción: Biblioteca para trabajar con nombres de dominio internacionalizados en aplicaciones Python.
  - Última versión probada: 3.6
  - Licencia: Licencia BSD

- **mailjet-rest**
  - Descripción: Cliente Python para la API REST de Mailjet.
  - Última versión probada: 1.3.4
  - Licencia: Licencia Apache-2.0

- **pillow**
  - Descripción: Biblioteca de procesamiento de imágenes para Python.
  - Última versión probada: 10.2.0
  - Licencia: Licencia PIL

- **python-dotenv**
  - Descripción: Carga configuraciones desde archivos .env en aplicaciones Python.
  - Última versión probada: 1.0.1
  - Licencia: Licencia MIT

- **requests**
  - Descripción: Biblioteca HTTP para Python.
  - Última versión probada: 2.31.0
  - Licencia: Licencia Apache-2.0

- **sqlparse**
  - Descripción: Análisis de SQL en Python.
  - Última versión probada: 0.4.4
  - Licencia: Licencia BSD

- **tzdata**
  - Descripción: Biblioteca de datos de zonas horarias de Python.
  - Última versión probada: 2024.1
  - Licencia: Dominio público

- **urllib3**
  - Descripción: Biblioteca HTTP para Python.
  - Última versión probada: 2.2.1
  - Licencia: Licencia MIT

#### Base de Datos:

- **SQLite**
  - Descripción: Sistema de gestión de bases de datos relacional ligero y rápido.
  - Última versión probada: Versión incluida con Python 3.x
  - Licencia: Dominio público



## Cómo contribuir
1. Envío de Pull Requests (PRs):

- Si tienes una nueva característica que te gustaría agregar o una corrección de errores que te gustaría realizar, ¡estamos abiertos a PRs! Por favor, sigue estas pautas al enviar tu PR:
    - Crea una rama nueva desde la rama `main`.
    Asegúrate de que tu código siga las guías de estilo del proyecto.

    - Incluye una descripción detallada de los cambios realizados en tu PR.

    - Asegúrate de que las pruebas unitarias estén pasando correctamente.

    - Si tu PR resuelve un problema específico, enlaza ese problema en la descripción del PR.

2. Reporte de Errores:
- Si encuentras algún error o problema en la herramienta,   por favor, abre un issue en el repositorio de GitHub. Asegúrate de incluir la mayor cantidad de detalles posible, incluyendo el comportamiento esperado y el comportamiento observado.

3. Guías de Estilo:
- Para mantener la consistencia en el código, sigue las guías de estilo definidas en el proyecto. Estas incluyen:

    - Seguir las convenciones de nomenclatura.
    - Utilizar espacios en blanco de manera consistente.
    - Mantener el código limpio y legible.
    - Comentar el código de manera adecuada para facilitar su comprensión.

*Puntos de Mejora:*
- Mejorar la documentación del código para facilitar su comprensión.

- Refactorizar partes del código para mejorar su rendimiento o claridad.

- Añadir nuevas características que puedan mejorar la funcionalidad y usabilidad de la herramienta.
Optimizar el código existente para reducir la complejidad y mejorar la mantenibilidad.

¡Tu contribución es importante para hacer crecer este proyecto! Estamos emocionados de recibir tus aportes y hacer de esta herramienta algo aún mejor.

## Código de conducta 
*Código de Conducta Contributor Covenant.*

*Código de Conducta de Citizen Code of Conduct.*

*Código de Conducta de Django.*

## Autor/es
<h3>Dextron03</h3>

## Información adicional
En este proyecto, se utiliza la API de MailJet para el envío de correos electrónicos debido a problemas con el servidor SMTP de Gmail en entornos de desarrollo. Con MailJet hice un pequeño servicio para el envío de correos electrónicos y otro para generar contraseñas aleatorias para cuando los usuarios quieran cambiar su contraseña y poder enviarlas por el correo electrónico que hayan seleccionado al registrarse.

## Variables de Entorno:
Antes de ejecutar la aplicación, asegúrate de configurar las siguientes variables de entorno en tu sistema:
`EMAIL_HOST_USER:` Esta variable deberá contener la dirección de correo electrónico que se utilizará como remitente para los correos electrónicos enviados por la aplicación. En este caso, se ha proporcionado la dirección de correo electrónico 'ejemplo@ejemplo.com'. Asegúrate de reemplazar esta dirección con la que desees utilizar en tu aplicación.

`API_KEY:` Esta variable deberá contener la clave de la API proporcionada por MailJet para autenticar las solicitudes de envío de correos electrónicos a través de su API. La clave '23jhk54h4j2jjk3j1123' es solo un ejemplo. Debes reemplazarla con la clave de API proporcionada por tu cuenta de MailJet.

`SECRET_KEY:` Esta variable deberá contener una clave secreta utilizada por Django para proporcionar seguridad en diversos aspectos de la aplicación, como la autenticación de usuarios y la protección contra ataques CSRF (Cross-Site Request Forgery). La clave '23jhk54h4j2jjk3j1123' es solo un ejemplo. Debes generar una clave segura y única para tu aplicación.

`SECRET_KEY_DJANGO:` Esta variable deberá contener la clave secreta utilizada por Django para el cifrado y la firma de cookies de sesión. Al igual que la variable SECRET_KEY, la clave 'django-insecure-=owovci_t950dg=d-dh&oaqdi!yo+#380+ev^8)v&r!p$vjsd=93' es solo un ejemplo y deberías generar una clave segura y única para tu aplicación.
