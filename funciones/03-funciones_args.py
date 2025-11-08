

def sumar(a, b):
    return a + b

def sumar_todos(*args):
    print(*args)
    resultado = 0
    for numero in args:
        resultado = resultado + numero
    return resultado

suma2 = sumar_todos(1, 2, 3, 4, 5)
print(suma2)

def calculadora(**kwargs):
    print(kwargs)
    if kwargs['operacion'] == 'suma':
        return kwargs['a'] + kwargs['b']
    elif kwargs['operacion'] == 'resta':
        return kwargs['a'] - kwargs['b']
    else:
        return 'Operación no soportada'
    
resultado1 = calculadora(operacion='suma', a=10, b=5)
print(resultado1)

resultado2 = calculadora(operacion='resta', a=10, b=5)
print(resultado2)