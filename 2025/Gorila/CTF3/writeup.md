WHY2025 CTF Writeup

**CTF Dates:**
🗓️ Fri, 08 Aug. 2025, 16:00 UTC — Mon, 11 Aug. 2025, 16:00 UTC

**Official URL:**
https://ctf.why2025.org/

**Challenge: Planets**

**Category: Web**

## 📝 Introducción del CTF:

    Take a cosmic stroll without leaving your chair! Our pocket-sized Solar System tour shows you each planet in all its glory—  fun facts, curious details, and zero risk of getting sucked into a black hole. 

// Básicamente lo que hace la página es mostrarte los planetas del sistema solar más una breve introducción educativa.

## Resolucion:

Para empezar a buscar pistas de como resolver el ctf vamos a inspeccionar el código fuente de la página y nos vamos a encontrar el siguiente script que es bastante revelador:

<img width="709" height="764" alt="Request" src="https://github.com/user-attachments/assets/979f52f2-a6c6-4ae6-969c-b1d537549e70" />

Como se puede observar la página para obtener los planetas le hace un request a la api "/api.php" la cual al recibir el json hace un query en la base de datos con el body de este a la tabla **Planets** la cual devuelve los planetas a la página. 

Al ver esto estamos ante un problema de inyección de sql básico, si encontramos una forma de enviarle manualmente código sql malicioso a la API entonces podríamos hacernos con los contenidos de la base de datos. Para ello voy a usar la aplicación burps porque se puede apreciar mejor lo que hacemos, después tienen un script más simplista que subimos a la carpeta por si quieren ir directo al grano.

Para empezar iniciamos burps, colocamos la página esta en **target** y después pusimos la request que le hace a la API para conseguir los planetas en repeater, eso nos va a permitir crear más peticiones POST manualmente, primero necesitamos saber que motor de bd usa la página, para ello iteramos con comandos que muestran la versión actual del motor, cada comando siendo de un motor diferente, hasta que al poner en el body **query=SELECT version()** nos retorno **{"version()":"8.0.42-0ubuntu0.24.04.2"}**;
Indicandonos que la base de datos usa MySQL, una vez sabido esto enviamos el siguiente payload para saber las tablas que tiene la bd **query=SELECT table_name FROM information_schema.tables**.

Y nos retorna lo siguiente:

<img width="1319" height="725" alt="PlanetasAbandonados" src="https://github.com/user-attachments/assets/c8fe4e40-8304-486e-b940-2c228d09d82c" />

Casi al final de la respuesta, nos damos cuenta que hay una tabla con un nombre bastante curioso **planetas abandonados**, para finalizar vamos a listar todos los elementos de esa tabla con un **query=select * from abandoned_planets** que nos retorna:

<img width="1366" height="758" alt="FlagPluto" src="https://github.com/user-attachments/assets/67ddf405-c9cc-4273-ac97-06641615d83f" />

Ahí nos muestra el planeta enano Plutón con la flag en la descripción.

> **vulnerabilidad:**
> Injection (https://owasp.org/Top10/A03_2021-Injection/)
