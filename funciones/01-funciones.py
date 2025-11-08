#Funciones

def saludar(nombre):
    """Funcion que saluda a una persona por su nombre"""
    return f"Hola {nombre}"
nombre_usuario = input("Hola, ¿como te llamas? ")

print(saludar(nombre_usuario))


def sumar(a, b):
    """Funcion que suma dos numeros"""
    suma = float(a) + float(b)
    return suma

numero1 = input("Ingresa el primer numero: ")
numero2 = input("Ingresa el segundo numero: ")
resultado = sumar(numero1, numero2)
print(f"El resultado de {numero1} + {numero2} = {resultado}")