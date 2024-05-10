import mysql.connector # 

base = mysql.connector.connect(host="localhost",user="root",password="marechal4093",database="ejemplo") #la contraseña para la conexion 
cursor= base.cursor()
sql="insert into clientes (DNI,Nombre,Apellido) values (%s,%s,%s)"
valores=(1111,'Juan','Lopez')
cursor.execute(sql,valores)
base.commit()