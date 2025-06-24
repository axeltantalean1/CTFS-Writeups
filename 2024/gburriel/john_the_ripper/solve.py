import subprocess
import os
import zipfile
import paramiko

# obtener el archivo via sftp

def connect_sftp(host, port, username, password):
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        return sftp, transport
    except Exception as e:
        print(f"Error conectando al SFTP: {e}")
        return None, None

def download_file(sftp, remote_folder, filename, local_folder):
    remote_path = f"{remote_folder}/{filename}"
    local_path = os.path.join(local_folder, filename)
    try:
        print(f"Descargando {remote_path} a {local_path}")
        sftp.get(remote_path, local_path)
        print("Descarga completa.")
    except Exception as e:
        print(f"Error descargando el archivo: {e}")

def disconnect_sftp(sftp, transport):
    if sftp:
        sftp.close()
    if transport:
        transport.close()

host = "200.58.100.246"
port = 22
username = "ftadmin"
password = "22031995" 

sftp = connect_sftp(host, port, username, password)

remote_folder = ".privado"
file_to_download = "flag.zip"
local_folder = os.path.dirname(os.path.abspath(__file__))

download_file(sftp, remote_folder, file_to_download, local_folder)

# descomprimir el archivo

zip_file = "flag.zip"
hash_file = "hash.txt"
zip2john = "zip2john.exe"
john = "john.exe"
rockyou_path = "rockyou.txt"
output_dir = "extraido"

for f in [zip_file, zip2john, john, rockyou_path]:
    if not os.path.isfile(f):
        print(f"No se encontró: {f}")
        exit(1)

with open(hash_file, "w") as f:
    print("Extrayendo hash con zip2john...")
    subprocess.run([zip2john, zip_file], stdout=f)

print("Corriendo John the Ripper con rockyou.txt")
subprocess.run([john, "--wordlist=" + rockyou_path, hash_file])

print("Mostrando contraseña si fue encontrada:")
result = subprocess.run([john, "--show", hash_file], capture_output=True, text=True)
output = result.stdout

password = None
for line in output.splitlines():
    if zip_file in line:
        parts = line.strip().split(":")
        if len(parts) > 1:
            password = parts[1]
            break

if password:
    print(f"Contraseña encontrada: {password}")
    try:
        with zipfile.ZipFile(zip_file) as zf:
            print(f"Extrayendo {zip_file} en '{output_dir}")
            os.makedirs(output_dir, exist_ok=True)
            zf.extractall(path=output_dir, pwd=password.encode())
            print("Extracción completada.")
    except RuntimeError as e:
        print(f"Falló la extracción: {e}")
else:
    print("No se encontró una contraseña válida")