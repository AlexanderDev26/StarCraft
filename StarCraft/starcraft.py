import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root", 
        database="starcraft"
    )
    
def crear_perfil():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== CREAR PERFIL DE JUGADOR ===")
    nombre = input("Ingrese su nombre de usuario: ")
    raza = input("Ingrese su raza preferida (Terran, Zerg, Protoss): ")
    nivel = input("Ingrese su nivel de habilidad (Principiante, Intermedio, Avanzado): ")

    try:
        sql = "INSERT INTO jugadores (nombre, raza, nivel_habilidad) VALUES (%s, %s, %s)"
        valores = (nombre, raza, nivel)
        cursor.execute(sql, valores)
        conexion.commit()

        print(f"Perfil creado exitosamente con ID {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def crear_partida():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== CREAR PARTIDA ===")
    tipo = input("Ingrese el tipo de partida (Clasificatoria, Amistosa, Cooperativa): ")
    jugadores = int(input("Ingrese el número de jugadores: "))
    mapa = input("Ingrese el mapa: ")

    try:
        sql = "INSERT INTO partidas (tipo_partida, numero_jugadores, mapa) VALUES (%s, %s, %s)"
        valores = (tipo, jugadores, mapa)
        cursor.execute(sql, valores)
        conexion.commit()

        print(f"Partida creada exitosamente con ID {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
        
#--------------------------funcion Read--------------------------------        
def listar_perfiles():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== LISTAR PERFILES DE JUGADORES ===")
    filtro = input("¿Desea filtrar por raza o nivel de habilidad? (S/N): ").strip().upper()

    if filtro == "S":
        criterio = input("Ingrese el criterio de filtro ('raza' o 'nivel'): ").strip().lower()
        valor = input("Ingrese el valor del filtro: ").strip()

        if criterio == "raza":
            sql = "SELECT * FROM jugadores WHERE raza = %s"
        elif criterio == "nivel":
            sql = "SELECT * FROM jugadores WHERE nivel_habilidad = %s"
        else:
            print("Criterio no válido. Mostrando todos los perfiles.")
            sql = "SELECT * FROM jugadores"
            valor = None
    else:
        sql = "SELECT * FROM jugadores"
        valor = None

    try:
        if valor:
            cursor.execute(sql, (valor,))
        else:
            cursor.execute(sql)
        
        resultados = cursor.fetchall()
        if resultados:
            for jugador in resultados:
                print(f"ID: {jugador[0]}, Nombre: {jugador[1]}, Raza: {jugador[2]}, Nivel: {jugador[3]}, Fecha: {jugador[4]}")
        else:
            print("No se encontraron jugadores.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()
        
def listar_partidas():
    conexion = conectar()
    cursor = conexion.cursor()

    print("\n=== LISTAR PARTIDAS ===")
    try:
        sql = "SELECT * FROM partidas ORDER BY fecha_creacion DESC"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if resultados:
            for partida in resultados:
                print(f"ID: {partida[0]}, Tipo: {partida[1]}, Jugadores: {partida[2]}, Mapa: {partida[3]}, Fecha: {partida[4]}")
        else:
            print("No se encontraron partidas registradas.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()



# ====================Menú principal==================
def menu_principal():
    while True:
        print("\n=== STARCRAFT MANAGEMENT SYSTEM ===")
        print("1. Crear Perfil de Jugador")
        print("2. Crear Partida")
        print("3. Listar Perfiles de Jugadores")
        print("4. Listar Partidas")
        print("5. Actualizar Perfil de Jugador")
        print("6. Actualizar Partida")
        print("7. Eliminar Perfil de Jugador")
        print("8. Eliminar Partida")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_perfil()
        elif opcion == "2":
            crear_partida()
        elif opcion == "3":
            listar_perfiles()
        elif opcion == "4":
            listar_partidas()
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")


menu_principal()
