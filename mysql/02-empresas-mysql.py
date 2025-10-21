import mysql.connector
from tabulate import tabulate

# creamos una conexión
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db_g5'
)

print(f'estas conectado a a la base de datos : {connection.database}')


# select 
empresa_cursor = connection.cursor()
empresa_cursor.execute('select * from empresa')
resultado = empresa_cursor.fetchall()
# print(resultado)}


# for registro in resultado:
#     print('*******************')
#     print(f'dni : {registro[1]}')

columnas = ['id','ruc','razon_social','nombre_comercial','direccion']

print(tabulate(resultado,headers=columnas,tablefmt='grid'))

#cerramos la conexión
connection.close()