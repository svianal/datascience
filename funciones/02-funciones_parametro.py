# PARAMETROS EN FUNCIONES
# UNA FUNCION PUEDE TRABAJAR CON DATOS EXTERNOS

#Ejemplo sin parametros
def saludar():
    print("Hola")

saludar()

#Con parametros
def potencia(base, exponente=2):
    return base ** exponente

print(potencia(3))
print(potencia(3, 4))

#Funcion con MULTIPLES retornos
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

suma, resta = operaciones(5, 10)
print(f"La suma es {suma} y la resta es {resta}")