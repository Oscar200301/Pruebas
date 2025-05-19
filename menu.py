print('Calculadora')
print('1- Suma')
print('2- Resta')
print('3- Multiplicacion')

numero = int(input('Elige una opcion: '))
if numero == 1:
    exec(open('Suma.py').read())
elif numero == 2:
    exec(open('Resta.py').read())
elif numero == 3:
    exec(open('Multiplicacion.py').read())
    
