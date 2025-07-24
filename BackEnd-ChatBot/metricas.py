from time import time
from services import dialogflow_service
from difflib import SequenceMatcher

# Configuración
SIMILARITY_THRESHOLD = 0.7

def calcular_similitud(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

test_data = [
   {"input": "¿Qué definición tiene la anonimización segun la LOPDP?", "expected_intent": "q39", "expected_response": " Descripción de Anonimización: La aplicación de medidas para impedir la identificación o reidentificación de una persona física se llevará a cabo sin incurrir en esfuerzos desproporcionados. Esto implica que las acciones de preservación de la privacidad se llevarán a cabo sin requerir recursos, tiempo o esfuerzos excesivos que no estén justificados por los beneficios o la finalidad perseguida."},
    {"input": "¿Qué definición tiene los datos biometricos segun la LOPDP", "expected_intent": "q40", "expected_response": "Descripción de Datos_biométricos:Datos personales únicos, relacionados con las características físicas o fisiológicas, o comportamientos de una persona física que permiten o confirman la identificación única de dicha persona, tales como imágenes faciales o datos dactilares, entre otros."},
    {"input": "¿Cuánto tiempo debe esperar el usuario ser notificado por vulnerabiliad en la transferencia de datos?", "expected_intent": "q3", "expected_response": "5 días"},
    {"input": "¿Cuáles son las sanciones por manejar incorrectamente la transferencia de información?", "expected_intent": "q4", "expected_response": "Leves: En el caso de la Autoridad de Datos, el rango es de 1 a 10 salarios básicos unificados; no se consideran los demás integrantes de la ley., Graves: En el caso de la Autoridad de Datos, el rango es de 10 a 20 salarios básicos unificados; no se consideran los demás integrantes de la ley., Muy graves: Infracciones que deben tener un tratamiento especial en función de la gravedad de la infracción."},
    {"input": "Qué significado tiene la entidad certificadora segun la LOPDP", "expected_intent": "q41", "expected_response": "Entidad que tiene capacidad para emitir certificaciones en materia de protección de datos de carácter personal, de forma no exclusiva, lo que significa que no es la única entidad con esta potestad, pudiendo otras organizaciones otorgar certificaciones en la misma materia."},
    {"input": "¿Qué datos se utilizan para la elaboración de perfiles?", "expected_intent": "q42", "expected_response": "Situación económica, sanidad, intereses, ubicación, otros aspectos similares, preferencias personales, movimiento físico, desempeño profesional, habilidades"},
    {"input": "¿Qué actividades puede realizar el encargado del tratamiento en relación con la transferencia de datos personales?", "expected_intent": "q7", "expected_response": "Descripción de las actividades del encargado del tratamiento en relación con la transferencia de datos personales: - Políticas de protección: Políticas de protección de datos que se aplicarán a los datos  - Seguridad de datos personales: El responsable y encargado de los datos personales es responsable de garantizar la seguridad de los datos del titular. - Mantenimiento de precisión: El responsable y el encargado son responsables de mantener la precisión de la información en los procesos de transferencia y verificación. - Reglas cooperativas vinculantes: El responsable y el encargado son responsables de la aplicación de las normas cooperativas vinculantes. - Metodologías de análisis: Metodología de análisis a utilizar sobre los datos."},
    {"input": "¿Quién es responsable de implementar medidas de seguridad adecuadas durante la transferencia de datos personales?", "expected_intent": "q8", "expected_response": "El responsable y encargado de los datos personales es responsable de garantizar la seguridad de los datos del titular."},
    {"input": "¿Quién es responsable de verificar la exactitud de la información transferida?", "expected_intent": "q10", "expected_response": "El responsable y el encargado son responsables de mantener la exactitud de la información en los procesos de transferencia y verificación."},
    {"input": "¿Qué acciones puede tomar el titular de los datos para verificar la información en poder del responsable del tratamiento?", "expected_intent": "q11", "expected_response": "El titular de los datos puede solicitar la verificación de su información al encargado o responsable del tratamiento de sus datos sin coste alguno y a la mayor brevedad posible."},
    {"input": "¿Cuáles son las consecuencias si los datos personales almacenados por el responsable están desactualizados o son inexactos?", "expected_intent": "q12", "expected_response": " Leve: Estas infracciones están en función de la infracción o falta del responsable del fichero. Por ejemplo, no tramitar o no aplicar un proceso en la transferencia de información se consideraría una infracción leve., Grave: Estas infracciones son acordes con la infracción o falta del responsable de los datos. Por ejemplo, si no se realiza un trámite administrativo., Muy Grave: No se especifica, pero si la hay, la Autoridad decide qué medidas tomar."},
    {"input": "¿Qué medidas de seguridad debe implementar el responsable del tratamiento para garantizar la integridad de los datos personales y evitar su modificación no autorizada?", "expected_intent": "q14", "expected_response": "- Verificación: Implementa procesos de verificación - Seguridad: El responsable y encargado de los datos personales es responsable de garantizar la seguridad de los datos del titular.- Políticas: Establece políticas de protección de datos- Metodologías: Coloca metodologías de análisis"},
    {"input": "¿Qué recursos tiene el titular de los datos si la información verificada es incorrecta o se está usando indebidamente?", "expected_intent": "q16", "expected_response": " Informado: El interesado debe estar informado en todo momento de la situación de sus datos y debe ser informado si se hace un uso indebido de los mismos."},
    {"input": "¿Cuál es el rol de la Autoridad de Protección de Datos Personales en la verificación de la información y el cumplimiento de las medidas de seguridad por parte del responsable del tratamiento?", "expected_intent": "q17", "expected_response": "Corrige los errores generados por los responsables en el proceso de transferencia de información."},
    {"input": "¿Cuáles son las excepciones destacadas relacionadas con el proceso de transferencia o comunicación?", "expected_intent": "q18", "expected_response": "Excepciones que pueden producirse en el proceso de transferencia de datos personales"},
    {"input": "¿Puedes explicarme qué significa el derecho de acceso?", "expected_intent": "q21", "expected_response": "Descripción del derecho de acceso: El titular tiene derecho a acceder y obtener gratuitamente todos sus datos personales, así como la información detallada de acuerdo con el derecho a la información, sin necesidad de justificación alguna."},
    {"input": "¿A partir de qué edad puedo dar mi consentimiento explícito para el tratamiento de mis datos personales?", "expected_intent": "q23", "expected_response": "Edad del titular: Personas cuya edad esté comprendida entre 15 y 17 años"},
    {"input": "¿Cuáles son las condiciones que hacen válido mi consentimiento y qué implica cada una?", "expected_intent": "q24", "expected_response": " Libre de vicios del consentimiento, Informado para garantizar la transparencia y el derecho a la información, Específico con respecto a los medios y fines del tratamiento, Inequívoca, sin dudas sobre la autorización concedida por el titular"},
    {"input": "¿Qué derechos tengo como titular de mis datos personales?", "expected_intent": "q26", "expected_response": "Plazo en días para el derecho de acceso: 15"},
    {
  "input": "¿Qué información debe comunicarse al titular en relación con el derecho a la información?",
  "expected_intent": "q27",
  "expected_response": "Debe comunicarse al titular la siguiente información:\n\n- Los fines del tratamiento.\n- La base jurídica del tratamiento.\n- La identidad y los datos de contacto del responsable del tratamiento de datos personales, incluyendo dirección, número de teléfono y correo electrónico.\n- La identidad y los datos de contacto del responsable de la protección de datos personales, si procede.\n- La existencia de una base de datos que contenga sus datos personales.\n- Los distintos tipos de tratamiento.\n- La existencia de evaluaciones y decisiones automatizadas, incluida la elaboración de perfiles.\n- El origen de los datos personales si no se han obtenido directamente del interesado.\n- El periodo durante el cual se conservarán los datos.\n- Las posibles consecuencias para el titular si facilita o se niega a facilitar sus datos personales.\n- Las repercusiones de facilitar datos personales incorrectos o inexactos.\n- La opción de revocar el consentimiento en cualquier momento.\n- Cómo ejercer sus derechos de acceso, supresión, rectificación, actualización, oposición, cancelación, limitación del tratamiento y a no ser objeto de decisiones automatizadas.\n- Cualquier otra finalidad o tratamiento adicional.\n- Dónde y cómo presentar reclamaciones ante el responsable del tratamiento y la Autoridad de Protección de Datos Personales."
}

]

# Métricas
correct_intent = 0
correct_response = 0
total = len(test_data)
times = []
total_correctos_completos = 0


print("Iniciando evaluación...\n")

for i, example in enumerate(test_data):
    user_input = example["input"]
    expected_intent = example["expected_intent"]
    expected_response = example["expected_response"]

    print(f"🔹 Prueba {i+1}: \"{user_input}\"")

    start = time()

    try:
        query_result = dialogflow_service.detect_intent_text(user_input)
        detected_intent = query_result.intent.display_name

        respuesta = dialogflow_service.process_intent(user_input)

        try:
            respuesta_traducida = dialogflow_service.translate_to_spanish(str(respuesta))
        except Exception as e:
            print(f"   ⚠️ Error al traducir: {e}")
            respuesta_traducida = str(respuesta)

        end = time()
        times.append(end - start)

        similitud = calcular_similitud(respuesta_traducida, expected_response)

        print(f"   → Intent detectado: {detected_intent}")
        print(f"   → Intent esperado:  {expected_intent}")
        print(f"   → Respuesta:         {respuesta_traducida}")
        print(f"   → Esperada:          {expected_response}")
        print(f"   → Similitud:         {similitud:.2f}")

        if detected_intent == expected_intent:
            correct_intent += 1
        else:
            print("   ❌ Intent incorrecto")

        if similitud >= SIMILARITY_THRESHOLD:
            correct_response += 1
        else:
            print("   ❌ Respuesta no suficientemente parecida")

        if detected_intent == expected_intent and similitud >= SIMILARITY_THRESHOLD:
            total_correctos_completos += 1

    except Exception as e:
        print(f"   💥 Error inesperado: {e}")
        continue

# Cálculos finales
precision = correct_response / total if total > 0 else 0
recall = correct_intent / total if total > 0 else 0
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
# avg_time = sum(times) / total if total > 0 else 0
accuracy = total_correctos_completos / total if total > 0 else 0

# Resultados
print("\n✅ Evaluación completa")
print(f"Total de pruebas: {total}")
print(f"Intents correctamente detectados: {correct_intent}")
print(f"Respuestas que superan el umbral: {correct_response}")
print(f"Precisión :  {precision:.2%}")
print(f"Recall : {recall:.2%}")
print(f"F1 Score :  {f1:.2%}")
print(f"Accuracy : {accuracy:.2%}")
# print(f"Tiempo promedio de respuesta:   {avg_time:.2f} s")
