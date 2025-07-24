import os

#configuracion para conexiones 
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'credentials/demochatbot-hpgt-73616510216e.json'

DB_CONFIG = {
    "dbname": "BotTest",
    "user": "postgres",
    "password": "admin",
    "host": "localhost",
    "port": "5432"
}

#variables generales
DIALOGFLOW_PROJECT_ID = "demochatbot-hpgt"
DIALOGFLOW_SESSION_ID = "UN_SESSION_ID_UNIC"
DEEPL_AUTH_KEY = "d9312f51-995a-45d6-bd57-2f641d7a1dd6:fx"
RDF_PATH = r'credentials/OntoPriv.rdf'
ONTO_PREFIX = "http://www.semanticweb.org/franc/ontologies/2023/9/OntologiaLOPDP#"
DATOSPERSONALES_PREFIX = "http://www.semanticweb.org/ley-organica-proteccion-datos-personales#"

