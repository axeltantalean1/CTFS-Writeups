import subprocess
import os

file = "toretto.bin"
mesen = r"C:\Program Files\Mesen\Mesen.exe" # hay que instalarlo, es un emulador de nes

result = subprocess.run(["file", file], capture_output=True, text=True, shell=True)
print("Resultado del comando 'file':")
print(result.stdout)

if not os.path.isfile(file):
    print(f"El archivo '{file}' no se encontró.")
else:
    print(f"Abriendo {file} con Mesen...")
    subprocess.Popen([mesen, file])