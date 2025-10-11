import os
from time import sleep

bandera = True
print("======== CALCULADORA CON PYTHON =========")
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

while bandera:
    os.system("clear")
    print("======== OPCIONES ========")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = int(input("Ingrese la opción que desea: "))
    
    if opcion == 1:
        print("======= SUMA =======")
        resultado = numero1 + numero2
        print(f"El resultado de la suma es: {resultado}")
    
    elif opcion == 2:
        print("======= RESTA =======")
        resultado = numero1 - numero2
        print(f"El resultado de la resta es: {resultado}")
    
    elif opcion == 3:
        print("======= MULTIPLICACIÓN =======")
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación es: {resultado}")
    
    elif opcion == 4:
        print("======= DIVISIÓN =======")
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado de la división es: {resultado}")
        else:
            print("No se puede dividir entre 0")
    
    elif opcion == 5:
        print("Saliendo del programa...")
        bandera = False
        sleep(2)
    else:
        print("Opción no válida. Intente de nuevo.")
