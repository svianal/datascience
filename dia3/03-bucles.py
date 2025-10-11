tabla = int(input("Ingrese la tabla que quiere multiplicar: "))


for contador in range(1, 10, 1):
    resultado = int(tabla * contador)
    print(f"{tabla} x {contador} = {resultado}")