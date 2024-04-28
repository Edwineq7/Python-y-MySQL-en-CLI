import mysql.connector

def connect_to_mysql():
    try:
        # Establecer la conexión
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Admin1",
            database="pos",
        )

        if conn.is_connected():
            print("Conexión establecida exitosamente")
            return conn

    except mysql.connector.Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def main():
    # Establecer conexión
    conn = connect_to_mysql()
    
    if conn:
        # Cerrar la conexión
        conn.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    main()
