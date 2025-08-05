import sys

# Abre el archivo y devuelve los caracteres
def file_to_chars(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    chars = ''.join(c for c in content if c.isalpha())
    return chars

# Convierte los caracteres a una cadena binaria
def chars_to_binary(chars, invert=False):
    binary = []
    for c in chars:
        if not invert:
            binary.append('1' if c.isupper() else '0')
        else:
            binary.append('0' if c.isupper() else '1')
    return ''.join(binary)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py archivo.txt [invert]")
        sys.exit(1)
    
    filename = sys.argv[1]
    invert = len(sys.argv) > 2 and sys.argv[2] == 'invert'

    chars = file_to_chars(filename)  
    binary = chars_to_binary(chars, invert)
    print(binary)