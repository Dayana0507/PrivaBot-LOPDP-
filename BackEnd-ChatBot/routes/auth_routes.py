from flask import Blueprint, request, jsonify
from services.user_service import find_user_by_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'error': 'Correo no enviado'}), 400

    try:
        user = find_user_by_email(email)
        if user:
            return jsonify({
                'id': user[0],
                'email': user[1],
                'message': 'Correo encontrado, ingreso válido'
            }), 200
        else:
            return jsonify({'message': 'Correo no registrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
