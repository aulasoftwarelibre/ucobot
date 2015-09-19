#Bot de alertas

Esta aplicación permite crear un bot para alertas en Telegram

##Instalación

###Dependencias

El desarrollo del bot se hará con python3. Así que lo primero es asegurarnos de que lo tenemos instalado:

```bash
bash$ sudo apt-get install -d python3 python3-pip
```

Se pueden instalar las dependencias en un subdirectorio o en el sistema. Se recomienda el primer método para evitar problemas:

```bash
bash$ pip3 install -t dist -r requirements.txt
```

###Alta de un bot

Para desarrollar, cada miembro puede crear su propio bot para desarrollo. Para ello [seguir el tutorial oficial](https://core.telegram.org/bots#botfather)

Es importante anotar el token de autorización de nuestro bot. Por ejemplo, consideremos que nuestro bot tiene el token ```110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw```.

###Configuración

Antes de iniciar el bot, tenemos que configurar el token. Para ello copiaremos el fichero _config/parameters.yml.dist_ en _config/parameters.yml_ añadiendo el token que hemos obtenido en el paso anterior. El fichero debe quedar así (pero con nuestro token):

```yaml
telegram:
    token: 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw
```

###Inicio del bot

Iniciamos el script de python _ucobot.py_.

###Demo

Podemos hablarle a nuestro bot que responderá, por ahora, a las órdenes _/start_ y _/help_.

##Desarrollo

Nos basaremos en dos APIs:

* Para Telegram Bot: [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
* Para la base de datos: [ponyorm](http://ponyorm.com/)

Cada grupo de órdenes tendrá un fichero independiente en el directorio _ucobot_ (ver commands.py como ejemplo).

Si es necesario guardar datos, se usara el ORM de Python PonyORM para definir las clases.
