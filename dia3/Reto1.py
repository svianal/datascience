#CREAR UN PROGRAMA USANDO COMO EJEMPLO EL CODIGO DE LA CALCULADORA QUE PERMITA CONVERTIR EL 
#VALOR DE UNA MONEDA DE SOLES A DOLARES Y VICEVERSA, POR EJEMPLO SI INGRESO CONVERTIR SOLES 
#A DOLARES E INGRESO 3000 SOLES DEBERIA MOSTRARME SU VALRO EN DOALRES QUE SERIA 1000 DOLARES 
#CONSIDERANDO QUE EL TIPO DE CAMBIO ES 3
import os
from time import sleep

print('Desea convertir de:')
print('1. Soles a dolares')
print('2. Dolares a soles')
respuesta = input(('Marque 1 o 2: '))
while (respuesta != '1' and respuesta != '2'):
    os.system('clear')
    respuesta = input(('Invalido, marque 1 o 2: '))

if(respuesta == '1'):
        monto = input(('Ingrese la cantidad de soles a convertir: '))
        resultado = float(monto)/3
        monedaInicial = 'soles'
        monedaFinal = 'dolares'
elif(respuesta == '2'):
        monto = input(('Ingrese la cantidad de dolares a convertir: '))
        resultado = float(monto)*3
        monedaInicial = 'dolares'
        monedaFinal = 'soles'
print(f"{monto} {monedaInicial} son {resultado} {monedaFinal}")
sleep(2)
