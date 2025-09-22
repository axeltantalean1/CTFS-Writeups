#!/usr/bin/env python3
import os, zipfile, subprocess, re

ZIP = "./recurso/SWAMP_D_image.zip"   
WORKDIR = "./work"            
OUT = "./foremost_out"


# Hacemos el unzip.
subprocess.run(["unzip", "-o", ZIP, "-d", WORKDIR], check=True)

# Encontramos el VHD
vhd = None
for root, _, files in os.walk(WORKDIR):
    for f in files:
        if f.lower().endswith(".vhd"):
            vhd = os.path.join(root, f)
            break
    if vhd: break

if not vhd:
    print("No VHD found")
    exit(1)

# Usamos foremost con ese VHD encontrado
subprocess.run(["foremost", "-i", vhd, "-o", OUT], check=True)

ZIP2 = "./foremost_out/zip/00041357.zip"

#hacemos el unzip del archivo donde esta la flag
subprocess.run(["unzip", "-o", ZIP2, "-d", WORKDIR], check=False)

subprocess.run([
    "grep",
    "-aoE",
    r"\{[^}]+\}",  # raw string para evitar problemas de escape
    "./work/word/document.xml"
])
