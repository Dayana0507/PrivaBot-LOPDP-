from flask import Blueprint, request, jsonify
from services.dialogflow_service import process_intent, translate_to_spanish

dialogflow_bp = Blueprint('dialogflow', __name__)

@dialogflow_bp.route('/dialogflow', methods=['POST'])
def dialogflow_api():
    user_text = request.json.get("message")
    if not user_text:
        return jsonify({"error": "No se recibió texto"}), 400

    respuesta = process_intent(user_text)
    respuesta_en_espanol = translate_to_spanish(respuesta)

    return jsonify({"response": respuesta_en_espanol})
