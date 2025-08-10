#!/usr/bin/env python3

import sys

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_chars_decrypt(text, pos):
    """Revierte el shift de caracteres (direccion contraria)"""
    out = ""
    for letter in text:
        if letter in alphabet:
            # Shift hacia atras
            letter_pos = (alphabet.find(letter) - pos) % 26
            new_letter = alphabet[letter_pos]
            out += new_letter
        else:
            out += letter
    return out

def decrypt_text(encrypted_text):
    """Desencripta el texto a la inversa"""
    counter = 0
    decrypted_text = ""
    
    # Procesar en chunks de 10 caracteres, igual que el original
    for i in range(0, len(encrypted_text), 10):
        counter = (counter + 1) % 26
        # Desencriptar el chunk actual
        chunk = encrypted_text[i:i+10]
        decrypted_chunk = shift_chars_decrypt(chunk, counter)
        decrypted_text += decrypted_chunk
    
    return decrypted_text

# Texto encriptado extraído del .pcap
encrypted_content = """Rfdjqf Cbfuct Scncf

Iqjuhglhqxw

Fsv xlj Sfqfi:

- 1 rgxmk olhk vm Rvuiqvm tmbbdln, lqxyyon
- 1 mez nczfezyd (tayqympq be fgber-ociuvh)
- 0,5 rje Ppgcuiqd sxuujv, jyrmvu gj yjslwv

Fhk max Dlymmcha:

- 0,5 xpk iwukjjweob (lo 0,5 asn kywm + 0,5 bto Greek yoguru gps b mjijvgt xgtulrq)
- 2 wfwt piqsr oznhj (kwjynre ywakkglk)
- 1 aax Dqrwv udbcjam
- 1 dcz Wybmodepcdstcp emgoq
- 1 tneyvp pybjs, awbqsr
- 2 pcrwdlo vybbuji, wzevcp tzghhwv (gj 0,5 mli thwbips jumoz, jkodjiwh)
- 0,25 zrm lifsb mgj
- Syjs & akzbj pepper, to ubtuf
- b ftkbbng qi iodj{dg1g53fj1i00e9239i29jifgjijg2964}

Iuzaybjaqwva

Mism cqn Danbbsxq

- Ix l mzhw, hsuew fasqftre znlbaanwgs, zsacb yjxrt, Dxzed ckijqhu, Wfitvjkwjkzajw ksnvx, fbgvxx aulfcw, viy vixcjqeao.
- Shktiv aofwwic gl rfc mkhud nhk vhile whiskjoh up fnvnukha.
- Agg vdow dqh tittiv xt yfxyj.

Pxkvgxk znl Shshk

- Iv i tizon bjujm kxgv, dycc mszaapo Rzxmuzq xqffgpr jvgu pecihcbg obr Ppgbthpc sxuuiu.

Ajjvdscv

- Djarrdw lax wkxllbga ipyl nby nvgvy viy cajphu pkpp ql zlxq ctcpwrfglf dudmkx.

Serve Immfejbufmz

- Gctpkuj zlwk hawud Pevqiwer fsi hwtzytty ol jkyoylk.
- Euqwg eqbp ozruunm lqrluox, crbswa, zc dlwxaz rad m bebgrva obbgh!"""

if __name__ == '__main__':
    print("=== DECRIPTANDO ===\n")
    
    decrypted = decrypt_text(encrypted_content)
    
    print("Texto decriptado:")
    print("-" * 50)
    print(decrypted)
    print("-" * 50)
    
    # Buscar la flag específicamente
    print("\nBuscando flag...")
    if "flag{" in decrypted.lower():
        lines = decrypted.split('\n')
        for line in lines:
            if "flag{" in line.lower():
                print(f"FLAG ENCONTRADA!: {line.strip()}")
