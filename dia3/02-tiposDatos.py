numero1 = int(input("Dame un numero "))
numero2 = int(input("Dame otro numero "))
operacion = input("Ingrese la operacion: +, -, * o / ")

if(operacion == "+"):
    resultado = numero1 + numero2
elif(operacion == "-"):
    resultado = numero1 - numero2
elif(operacion == "*"):
    resultado = numero1 * numero2
elif(operacion == "/"):
    resultado = numero1 / numero2
else:
    resultado = "No es un operador valido"

print(str(resultado))