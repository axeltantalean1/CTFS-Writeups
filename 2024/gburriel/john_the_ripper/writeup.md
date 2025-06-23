EkoParty 2024

En este desafío lo primero que daban es el enlace a una cuenta de twitter que tenía 4 tweets.

![](img1.png)

Haciendo cuentas con la fecha del segundo tweet (de abajo para arriba) llegué a la conclusión de que nació el 22 de marzo de 1995. Esto debido a que si faltan 165 dias cumple el 22 de marzo. Y como fue en 2024 quiere decir que cumple 30 en 2025, o sea que es de 1995. La contraseña que se ve en el tercer tweet tiene 8 digitos. Al probar la fecha de nacimiento (22031995) en el comando sftp que se ve en el cuarto tweet pude descargar un archivo llamado flag.zip.

Hice un script para probar las contraseñas del famoso rockyou.txt pero ninguna funcionó. Mi siguiente decisión fue probar algunos comandos para ver si encontraba algo extra. Al probar con exiftool pude ver que había una imagen llamada rockyou.jpg. Como sentí que iba relacionado con lo que venía probando busqué otra herramienta y encontré una llamada John the Ripper. Me descargué zip2john y lo usé con el rockyou.txt. Al hacer esto obtuve como respuesta "november".

Luego, probé la contraseña november en el .zip que había descargado y pude ver el contenido del mismo, donde estaba la flag.

Finalmente, hice un script que automatice ambas partes. Primero, la conexión sftp con la respectiva descarga del archivo 'flag.zip'. Luego, el uso de zip2john para, por medio del rockyou.txt, obtener la contraseña, descomprimir el archivo, y obtener la flag.

![](img2.png)