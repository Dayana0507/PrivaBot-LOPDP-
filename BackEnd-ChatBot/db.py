import psycopg2
from psycopg2.extras import DictCursor
from config import DB_CONFIG

#conexion bd 
def get_connection():
    conn = psycopg2.connect(
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"]
    )
    return conn

def get_cursor(dict_cursor=False):
    conn = get_connection()
    if dict_cursor:
        return conn, conn.cursor(cursor_factory=DictCursor)
    else:
        return conn, conn.cursor()
