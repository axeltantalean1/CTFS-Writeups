from sympy.ntheory import discrete_log

def main():
    p = 14912432766367177751
    g = 2784687438861268863
    h = 8201777436716393968
    c1 = 12279519522290406516
    c2 = 10734305369677133991

    # Paso 1: Calcular la clave privada x (logaritmo discreto)
    x = discrete_log(p, h, g)
    print(f"[+] Clave privada x = {x}")

    # Paso 2: Descifrar el mensaje
    s = pow(c1, x, p)
    inv_s = pow(s, -1, p)
    m = (c2 * inv_s) % p
    print(f"[+] Mensaje (entero) m = {m}")

    # Paso 3: Convertir m a texto
    byte_length = (m.bit_length() + 7) // 8
    flag_bytes = m.to_bytes(byte_length, 'big')
    flag = flag_bytes.decode('ascii')
    print(f"[+] Flag: brunner{{{flag}}}")

if __name__ == '__main__':
    main()

