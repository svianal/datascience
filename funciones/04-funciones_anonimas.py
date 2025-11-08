#FUNCIONES ANONIMAS
#reservadas con la palabra LAMBDA

sumar2 = lambda a, b: a + b
print(sumar2(3, 4))

multiplicar = lambda a, b: a * b
print(multiplicar(3, 3))

division = lambda a, b: a / b if b != 0 else "No se puede dividir por cero"
print(division(6, 2))