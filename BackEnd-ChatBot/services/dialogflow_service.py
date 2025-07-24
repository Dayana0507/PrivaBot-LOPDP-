from google.cloud import dialogflow_v2 as dialogflow
from config import DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID, DEEPL_AUTH_KEY
import deepl
from Querys.queryHandlerQ import QueryHandlerQ

#logica para consultar solo metodos de dialog flow
session_client = dialogflow.SessionsClient()
session_path = session_client.session_path(DIALOGFLOW_PROJECT_ID, DIALOGFLOW_SESSION_ID)
query_handler = QueryHandlerQ()
translator = deepl.Translator(DEEPL_AUTH_KEY)

def detect_intent_text(text):
    text_input = dialogflow.TextInput(text=text, language_code="en")
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session_path, "query_input": query_input}
    )
    return response.query_result

def process_intent(user_text):
    query_result = detect_intent_text(user_text)
    intent_name = query_result.intent.display_name
    respuesta = query_result.fulfillment_text

    # Mapping dinámico con validación de existencia de métodos
    intent_to_function = {}

    for i in range(1, 50):
        method_name = f"q{i}"
        if hasattr(query_handler, method_name):
            intent_to_function[method_name] = getattr(query_handler, method_name)

    for i in range(1, 51):
        method_name = f"s{i}"
        if hasattr(query_handler.queryHandlerS, method_name):
            intent_to_function[method_name] = getattr(query_handler.queryHandlerS, method_name)

    for i in range(51, 101):
        method_name = f"t{i}"
        if hasattr(query_handler.queryHandlerT, method_name):
            intent_to_function[method_name] = getattr(query_handler.queryHandlerT, method_name)

    for i in range(101,151):
        method_name = f"t{i}"
        if hasattr(query_handler.queryHandlerU, method_name):
            intent_to_function[method_name] = getattr(query_handler.queryHandlerU, method_name)

    if intent_name in intent_to_function:
        try:
            respuesta = intent_to_function[intent_name]()
        except Exception as e:
            respuesta = f"Error al procesar la intención {intent_name}: {str(e)}"

    return respuesta


def translate_to_spanish(text):
    result = translator.translate_text(text, target_lang="ES")
    return result.text
