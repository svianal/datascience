import os
from time import sleep

# EJERCIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE : SAMUEL VIANA

dic_empresas = {
    '20454545':{
        'razon_social': 'EMPRESA SAC',
        'direccion':'CALLE EL SOL 123',
    }
}

ANCHO = 50

while(True):
    os.system("clear")
    print("="*ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("="*ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)
    opcion = int(input("INGRESE OPCION : "))
    os.system("clear")
    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el Nro de RUC:")
        razon_social = input("Ingrese la razón social: ")
        direccion = input("Ingrese la dirección: ")
        dic_nueva_empresa = {
            'razon_social': razon_social,
            'direccion': direccion 
        }
        dic_empresas[ruc] = dic_nueva_empresa
    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)
        for ruc, info in dic_empresas.items():
            print(f"RUC : {ruc}" )
            print(f"Razon social : {info['razon_social']}")
            print(f"direccion : {info['direccion']}")
            print("------------------------")
    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc_actualizar = input("Ingrese el RUC de la empresa a actualizar: ")
        if ruc_actualizar in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc_actualizar]['razon_social']}")
            nueva_razon_social = input("Ingrese la nueva razon social")
            nueva_direccion = input("Ingrese la nueva direccion")
            if nueva_razon_social:
                dic_empresas[ruc_actualizar]['razon_social'] = nueva_razon_social
            if nueva_direccion:
                dic_empresas[ruc_actualizar]['direccion'] = nueva_direccion
    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc_actualizar = input("Ingrese el RUC de la empresa a eliminar: ")
        if ruc_actualizar in dic_empresas:
            print(f"Empresa encontrada: {dic_empresas[ruc_actualizar]['razon_social']}")
            #dic_empresas.pop(ruc_actualizar)
            del dic_empresas[ruc_actualizar]
            print("Empresa eliminada")
    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")
    