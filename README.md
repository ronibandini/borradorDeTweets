# borradorDeTweets
Script Python para eliminar tweets en masa utilizando el archivo de backup tweets.js 

Adapta el repositorio https://github.com/QuincyLarson/delete-tweets para utilizar Python 3 y las columnas del archivo de Backup tweet.js

# Instrucciones

1 Conseguir las API keys de Twitter El link es https://apps.twitter.com/app/new y cargarlas en el código Python

api = twitter.Api(consumer_key="123456",
                      consumer_secret="123456",
                      access_token_key="123456",
                      access_token_secret="123456")

2 Descargar un backup de todos los tweets. El link es https://twitter.com/settings/your_twitter_data

3 Descomprimir el backup, extraer /data/tweet.js 

4. Convertir a CSV desde https://tweetjstocsv.glitch.me/ y cargar el CSV en la carpeta del código Python

5 Ejecutar $ python deletetweets.py 
