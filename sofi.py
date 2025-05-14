import mysql.connector

DB_HOST = "localhost"  # Reemplaza con la dirección de tu servidor MySQL
DB_USER = "root"        # Reemplaza con tu nombre de usuario de MySQL
DB_PASSWORD = "root"    # Reemplaza con tu contraseña de MySQL
DB_NAME = "sofi"   # Reemplaza con el nombre de tu base de datos

try:
    # 1. Intenta establecer una conexión a la base de datos MySQL
    conexion = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


    # 2. Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()


    # 3. Define la consulta SQL para seleccionar los nombres de los estudiantes de 'Informática'
    consulta = "SELECT nombre FROM estudiantes WHERE materia= %s"
    valor_materia = ('Matematicas',)


    # 4. Ejecuta la consulta SQL
    cursor.execute(consulta, valor_materia)


    # 5. Obtén todos los resultados de la consulta
    resultados = cursor.fetchall()


    # 6. Itera sobre los resultados e imprime el nombre de cada estudiante
    print("Estudiantes de la materia de Matematicas:")
    for estudiante in resultados:
        print(estudiante[0])

except mysql.connector.Error as error:
    print("Error al conectar a MySQL: {error}")


finally:
    # 7. Cierra el cursor y la conexión a la base de datos (si se establecieron)
    if conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión a MySQL cerrada.")