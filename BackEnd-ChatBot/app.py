from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_bp
from routes.dialogflow_routes import dialogflow_bp
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

# Registrar blueprints (módulos de rutas)
app.register_blueprint(auth_bp)
app.register_blueprint(dialogflow_bp)
app.register_blueprint(chat_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
