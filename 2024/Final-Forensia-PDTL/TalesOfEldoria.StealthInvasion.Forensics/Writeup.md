Segundo desafío: Stealth Invasion - Hack the Box Tales of Eldoria (Forensics)

El desafío nos proporciona un memdump.elf y está estructurado como un conjunto de 6 flags a recuperar.

El primer desafío pide el primer proceso de Chrome que fue ejecutado, el cual encontramos utilizando volatility, filtrando por chrome.exe con la opción de windows.pslist

vol -f memdump.elf --filters "ImageFileName,chrome.exe" windows.pslist

Obtenemos:
PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	File output

4080	5296	chrome.exe	0xa708c729e0c0	48	-	1	False	2025-03-13 17:01:04.000000 UTC	N/A	Disabled
2736	4080	chrome.exe	0xa708c74560c0	11	-	1	False	2025-03-13 17:01:04.000000 UTC	N/A	Disabled
5688	4080	chrome.exe	0xa708c6cf4080	18	-	1	False	2025-03-13 17:01:04.000000 UTC	N/A	Disabled
7504	4080	chrome.exe	0xa708c6b19080	24	-	1	False	2025-03-13 17:01:04.000000 UTC	N/A	Disabled
1220	4080	chrome.exe	0xa708c7514080	9	-	1	False	2025-03-13 17:01:04.000000 UTC	N/A	Disabled
4612	4080	chrome.exe	0xa708c7230080	15	-	1	False	2025-03-13 17:01:05.000000 UTC	N/A	Disabled
8036	4080	chrome.exe	0xa708caec6080	13	-	1	False	2025-03-13 17:01:08.000000 UTC	N/A	Disabled
1368	4080	chrome.exe	0xa708c6594080	14	-	1	False	2025-03-13 17:01:11.000000 UTC	N/A	Disabled


Respuesta: El padre de todos es el proceso con PID 4080, el que creó al resto de procesos.



El segundo desafío pregunta cual es la única carpeta que está en el escritorio. Se podía sacar también con un grep, en mi caso usé volatility con windows.filescan, por consistencia.

vol -f memdump.elf windows.filescan.FileScan | grep -i Desktop

Obtenemos:

0xa708c8d9ec30	\Users\selene\Desktop\malext\background.js
0xa708c8d9fef0	\Users\selene\Desktop\malext\manifest.json
0xa708c8da14d0	\Users\selene\Desktop\malext\rules.json
0xa708c8da1e30	\Users\selene\Desktop\malext\content-script.js


Respuesta: malext.


El tercer desafío pregunta por el ID de la extensión maliciosa. Se busca simplemente con un grep por la palabra Extensions.

vol -f memdump.elf windows.filescan | grep -i "Extensions"

En este caso hay varias extensiones, pero nos interesa la que posee una carpeta con logs:

0xa708c8830c80 \Users\selene\AppData\Local\Google\Chrome\User Data\Default\Local Extension Settings\nnjofihdjilebhiiemfmdlpbdkbjcpae\LOG


Respuesta: nnjofihdjilebhiiemfmdlpbdkbjcpae.


El cuarto desafío pide encontrar el log en la extensión maliciosa donde se guarda la actividad sospechosa.

Hay varios logs, el que contiene la información sospechosa es 0000003.log.

El quinto desafío y el sexto desafío preguntaban por el sitio al que accedió el usuario y la contraseña del mismo, respectivamente. Ambos datos se hallan en el log anteriormente mencionado con lo que parece ser un keylogger.


Respuesta: Sitio accedido: drive.google.com
Respuesta: Password de Selene: clip-mummify-proofs.
