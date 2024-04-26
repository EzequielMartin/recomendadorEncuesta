# Descripcion:

Esta versión esta hecha para ejecutarse desde la encuesta en Dialogflow, cuando se termina de responder la encuesta se envian los parametros al servidor web desarrollado en NodeJS. Desde una llamada en el servidor web se ejecuta este programa en Python donde se obtiene el proyecto recomendado, luego se le retorna la respuesta a la funcion en el servidor web y este le responde al usuario a travez del chatbot.

  

# Para correrlo:

  

#### Tener la versión de python3.8 o superior instalada

  

	python3 --version

>si no funciona en vez de "python3" probar "py" o "python"

  

#### Crear un entorno virtual usando el comando

  

	python3 -m venv <environment_name>

  

>un nombre común usado es: .venv

>como comenté anteriormente si no funciona probar con "python" o "py" en vez de "python3"

  

#### Activar entorno virtual

  

	source <environment_name>/bin/activate

  

>yo para activarlo tuve que correr `.\.venv\Scripts\activate` , si no funciona probar así

  

#### Instalar los requirements

  

	pip install -r requirements.txt

  

#### Ejecutar el codigo con

  

	python3 main.py ia programacion infraestructura analisis diseno

  

>como comenté anteriormente si no funciona probar con "python" o "py" en vez de "python3".

>"ia" "programacion" etc. son los parametros que hay que pasarle al programa para que calcule
>que tanto se asemejan a las necesidades de los proyectos y poder recomendar el mas adecuado.