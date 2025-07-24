from db import get_connection

#metodo para consultar datos del usuario
def find_user_by_email(email):
    conn, cursor = get_connection(), None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, email FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        return user
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
