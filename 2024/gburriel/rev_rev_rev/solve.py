with open('output.txt', 'r') as file:
    z = eval(file.read()) 

y = [~i for i in z] # deshacer complemento a 1

x = [i ^ 0xff for i in y] # deshacer xor volviendo a aplicar

x.reverse() # volver a invertir el orden

flag = ''.join(chr(i) for i in x) # convertir de nuevo los caracteres

with open('flag.txt', 'w') as f:
    f.write(flag)