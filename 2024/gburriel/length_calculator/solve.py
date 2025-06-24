import socket

host = '34.146.219.32'
port = 33334

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print(f"Conectado a {host}:{port}")

    respuesta = s.recv(4096).decode()
    print(f"[Server] {respuesta.strip()}")

    if "enter size" in respuesta.lower():
        s.sendall(b'0\n')
        print("Enviado: 0")

        data_total = ''
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            data_total += chunk.decode()

        print("[Server] Respuesta final completa:")
        print(data_total.strip())

    else:
        print("[!] No se recibió 'enter size' como se esperaba")
