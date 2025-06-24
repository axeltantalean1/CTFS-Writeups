import zipfile
import os
import subprocess

with zipfile.ZipFile('faraday.zip', 'r') as zip_ref:
    zip_ref.extractall('faraday_extracted')

gb_path = 'faraday_extracted/llama_secret.gb'

result = subprocess.run(['strings', gb_path], capture_output=True, text=True)
print(result.stdout)