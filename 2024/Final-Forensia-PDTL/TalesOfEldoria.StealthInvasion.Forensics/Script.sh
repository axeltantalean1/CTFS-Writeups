#!/bin/bash

# Flag 1: buscar proceso chrome.exe
vol -f memdump.elf --filters "ImageFileName,chrome.exe" windows.pslist


#Flag 2: Buscar por coincidencias con Desktop para encontrar la carpeta dentro del mismo.
vol -f memdump.elf windows.filescan.FileScan | grep -i Desktop


# Flag 3: buscar archivos relacionados con Extensions
vol -f ./recurso/memdump.elf windows.filescan | grep -i "Extensions"

