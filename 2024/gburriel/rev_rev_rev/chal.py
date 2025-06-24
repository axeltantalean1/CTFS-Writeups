flag = open('flag.txt', 'r').read()
x = [ord(c) for c in flag] # obtener los ascii de cada caracter
x.reverse() # invertir el orden
y = [i^0xff for i in x] # xor
z = [~i for i in y] # complemento a 1
open('output.txt', 'w').write(str(z))
