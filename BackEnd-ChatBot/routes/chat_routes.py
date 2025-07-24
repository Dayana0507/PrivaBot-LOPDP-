from flask import Blueprint, request, jsonify
from services.chat_service import save_chat_history, get_chat_history_by_user

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/insertarChatHistorico', methods=['POST'])
def insertar_chat_historico():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No se recibieron datos JSON"}), 400

    id_user = data.get('id_user')
    email = data.get('email')
    chat_log = data.get('chatLog')

    if not id_user or not email or not isinstance(chat_log, list):
        return jsonify({"error": "Datos incompletos o mal formateados"}), 400

    try:
        save_chat_history(id_user, email, chat_log)
        return jsonify({"message": "Chat histórico guardado correctamente"}), 200
    except Exception:
        return jsonify({"error": "Error interno del servidor"}), 500

@chat_bp.route('/ConsultaHistoricoDetalle', methods=['GET'])
def obtener_historico_por_usuario():
    id_user = request.args.get('id_user')
    if not id_user:
        return jsonify({"error": "Se requiere el parámetro 'id_user'"}), 400

    try:
        historico = get_chat_history_by_user(id_user)
        return jsonify(historico), 200
    except Exception:
        return jsonify({"error": "Error interno del servidor"}), 500
