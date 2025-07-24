import json
from datetime import datetime
from psycopg2.extras import DictCursor
from db import get_connection


#logica para chatbot
def save_chat_history(id_user, email, chat_log):
    conn, cursor = get_connection(), None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM chatHistorico WHERE id_user = %s", (id_user,))
        result = cursor.fetchone()

        if result:
            chathist_id = result[0]
        else:
            cursor.execute(
                "INSERT INTO chatHistorico (id_user, email) VALUES (%s, %s) RETURNING id",
                (id_user, email)
            )
            chathist_id = cursor.fetchone()[0]

        chat_log_str = json.dumps(chat_log, ensure_ascii=False)
        now = datetime.now()
        cursor.execute(
            "INSERT INTO chatDetailHistorico (id_chathistorico, historial, fecha) VALUES (%s, %s, %s)",
            (chathist_id, chat_log_str, now)
        )
        conn.commit()
        return True
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_chat_history_by_user(id_user, limit=10):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=DictCursor)
    try:
        query = """
            SELECT 
                d.id AS detalle_id,
                d.id_chathistorico,
                d.historial,
                d.fecha,
                h.id_user,
                h.email
            FROM chatDetailHistorico d
            JOIN chatHistorico h ON d.id_chathistorico = h.id
            WHERE h.id_user = %s
            ORDER BY d.id DESC
            LIMIT %s;
        """
        cursor.execute(query, (id_user, limit))
        results = cursor.fetchall()
        historico = []
        for row in results:
            historico.append({
                "detalle_id": row["detalle_id"],
                "id_chathistorico": row["id_chathistorico"],
                "historial": row["historial"],
                "fecha": row["fecha"].isoformat(),
                "id_user": row["id_user"],
                "email": row["email"]
            })
        return historico
    finally:
        cursor.close()
        conn.close()
