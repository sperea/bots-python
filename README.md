# bots-python

Script de eliminación de Tweets en Twitter
==========================================

Este script de Python te permite eliminar todos los Tweets de tu cuenta de Twitter de manera automatizada. Es útil si deseas borrar todos tus Tweets antiguos o comenzar con una cuenta de Twitter nueva.

Requisitos
----------

* Python 3.x
* Biblioteca `selenium` (instalable mediante `pip install selenium`)
* WebDriver compatible con el navegador Chrome (se utiliza `webdriver_manager` para gestionar el WebDriver)

Configuración
-------------

1.  Instala las dependencias requeridas ejecutando el siguiente comando:
    
    Copy code
    
    `pip install selenium` 
    
2.  Asegúrate de tener el WebDriver adecuado para el navegador Chrome. Este script utiliza `webdriver_manager` para descargar automáticamente el WebDriver compatible. No es necesario realizar ninguna configuración adicional.
    

Uso
---

1.  Abre el archivo del script y reemplaza las variables `email` y `password` con tus credenciales de inicio de sesión de Twitter.
    
2.  Ejecuta el script `delete_tweets.py` en tu entorno Python.
    
    Copy code
    
    `python delete_tweets.py` 
    
3.  El script iniciará sesión en tu cuenta de Twitter y eliminará todos los Tweets de forma automática. Asegúrate de tener en cuenta que este proceso no se puede deshacer, y todos tus Tweets serán eliminados permanentemente.
    
4.  Una vez finalizada la ejecución del script, todos los Tweets de tu cuenta de Twitter habrán sido eliminados.
    

Advertencia
-----------

* Ten en cuenta que este script elimina todos los Tweets de tu cuenta de Twitter. Asegúrate de hacer una copia de seguridad o guardar cualquier Tweet importante antes de ejecutar el script.
    
* Este script está sujeto a las políticas y límites establecidos por Twitter. El uso excesivo o inapropiado de este script puede resultar en restricciones o suspensiones de tu cuenta de Twitter.
    

Licencia
--------

Este script se distribuye bajo la licencia GNU General Public License versión 3. Consulta el archivo [LICENSE](LICENSE) para más detalles.

**¡Utiliza este script con precaución y bajo tu propia responsabilidad!** Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

Mastodon to Twitter Bot
=======================

Este script te permite publicar toots de Mastodon en tu cuenta de Twitter automáticamente. Puedes seleccionar los toots que deseas compartir en Twitter y configurar la programación para que el proceso se ejecute de forma periódica.

Requisitos
----------

* Python 3.6 o superior
* Biblioteca `selenium` (instalable mediante `pip install selenium`)
* Biblioteca `python-dotenv` (instalable mediante `pip install python-dotenv`)
* WebDriver compatible con el navegador Chrome (consultar la documentación de Selenium para obtener detalles sobre la versión adecuada)

Configuración
-------------

1.  Crea un archivo `.env` en el mismo directorio que el script. Dentro de este archivo, define las siguientes variables de entorno:
    
    makefileCopy code
    
    `mastodon_client_id=TU_CLIENT_ID
    mastodon_client_secret=TU_CLIENT_SECRET
    mastodon_access_token=TU_ACCESS_TOKEN
    twitter_api_key=TU_API_KEY
    twitter_api_secret=TU_API_SECRET
    twitter_access_token=TU_ACCESS_TOKEN
    twitter_access_token_secret=TU_ACCESS_TOKEN_SECRET` 
    
    Asegúrate de reemplazar `TU_CLIENT_ID`, `TU_CLIENT_SECRET`, `TU_ACCESS_TOKEN`, `TU_API_KEY`, `TU_API_SECRET`, `TU_ACCESS_TOKEN`, y `TU_ACCESS_TOKEN_SECRET` con tus propias credenciales.
    
2.  Configura el WebDriver en el archivo `mastodon_to_twitter.py`. Asegúrate de que la ruta del WebDriver sea correcta y coincida con la versión y ubicación de tu WebDriver instalado.
    

Uso
---

1.  Ejecuta el script `mastodon_to_twitter.py` en tu entorno Python.
    
    Copy code
    
    `python mastodon_to_twitter.py` 
    
2.  El script cargará los toots desde Mastodon y los mostrará en la consola. Puedes seleccionar los toots que deseas publicar en Twitter ingresando el número correspondiente a cada toot.
    
3.  Después de seleccionar los toots, el script los publicará automáticamente en tu cuenta de Twitter.
    
4.  El proceso se puede programar para que se ejecute periódicamente utilizando una herramienta externa, como `cron` en sistemas Unix, o mediante una tarea programada en Windows.
    

Contribuciones
--------------

¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor crea un Pull Request con tus mejoras o soluciones a problemas existentes.

Licencia
--------

Este script está bajo la licencia MIT. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles.

¡Disfruta utilizando el Mastodon to Twitter Bot! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.

Twitter Tweet Deletion Script
=============================

This Python script allows you to delete all your tweets on Twitter automatically. It utilizes the Selenium library to interact with the Twitter website and perform the deletion process.

License
-------

This script is licensed under the GNU General Public License version 3. You can find the full text of the license in the [LICENSE](LICENSE) file.

Prerequisites
-------------

* Python 3.x
* Selenium library (installable via `pip install selenium`)
* Chrome WebDriver (used `webdriver_manager` to manage the WebDriver)

Setup
-----

1.  Install the required dependencies by running the following command:
    
    Copy code
    
    `pip install selenium` 
    
2.  Make sure you have the appropriate Chrome WebDriver installed. This script uses `webdriver_manager` to automatically download and manage the compatible WebDriver. No additional setup is required.
    

Usage
-----

1.  Open the script file `delete_tweets.py` and replace the `email` and `password` variables with your Twitter login credentials.
    
2.  Run the script `delete_tweets.py` in your Python environment.
    
    Copy code
    
    `python delete_tweets.py` 
    
3.  The script will open the Twitter login page and automatically sign in using the provided credentials.
    
4.  After successful login, the script will navigate to your Twitter profile page and start deleting all your tweets.
    
5.  Please note that the deletion process cannot be undone, and all your tweets will be permanently deleted.
    

Warning
-------

* Be aware that this script deletes all your tweets on Twitter. Make sure to backup or save any important tweets before running the script.
    
* This script is subject to Twitter's policies and limits. Excessive or inappropriate use of this script may result in restrictions or suspension of your Twitter account.
    

Contributions
-------------

Contributions to this project are welcome. Feel free to submit a pull request with your improvements or bug fixes.

Support
-------

If you have any questions or need assistance, please feel free to contact me.

**Use this script with caution and at your own risk!**