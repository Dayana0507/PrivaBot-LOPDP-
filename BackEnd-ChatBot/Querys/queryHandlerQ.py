from rdflib import Graph
from Querys.baseQueryHandler import BaseQueryHandler
from config import RDF_PATH, ONTO_PREFIX,DATOSPERSONALES_PREFIX
from Querys.queryHandlerS import QueryHandlerS
from Querys.queryHandlerT import QueryHandlerT
from Querys.queryHandlerU import QueryHandlerU

class QueryHandlerQ(BaseQueryHandler):
    def __init__(self):
        graph = Graph()
        graph.parse(RDF_PATH, format="xml")
        super().__init__(graph)
        self.queryHandlerS = QueryHandlerS(self.graph)
        self.queryHandlerT = QueryHandlerT(self.graph)
        self.queryHandlerU = QueryHandlerU(self.graph) 

    def q1(self):
        return "Consulta q1 aún no implementada."

    def q2(self):
        return "Consulta q2 aún no implementada."

    def q3(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?notification
            WHERE {{
                ?n a :Notification .
                ?n :Security_notification_of_infringement ?notification .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return str(row.notification)
        return "No se encontraron resultados."

    def q4(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?slight ?serious ?verySerious
            WHERE {{
                ?v a :Violations_in_verification .
                ?v :Penalties_for_serious_infractions ?serious .
                ?v :Penalties_for_mild_infractions ?slight .
                ?v :Very_serious ?verySerious .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            return f"Leves: {row.slight}, Graves: {row.serious}, Muy graves: {row.verySerious}"
        return "No se encontraron resultados."

    def q5(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?st
            WHERE {{
                ?il a :Legal_interest_in_verification .
                ?il :Specific_threats ?st .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            # return f"Interés legal: {row.il}, Amenazas específicas: {row.st}"
            return f"Amenazas específicas: {row.st}"
        return "No se encontraron resultados."

    def q6(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?mv ?ev ?process
            WHERE {{
                ?mv a :Members_of_the_protection_system_in_verification .
                ?mv :Perform_evaluations ?ev .
                ?mv :Implementing_verification_processes ?process .
            }}
        """
        try:
            result = self.graph.query(query)
            for row in result:
                return (
                    f"Miembro del sistema: {row.mv}\n"
                    f"- Evaluaciones realizadas: {row.ev}\n"
                    f"- Procesos implementados: {row.process}"
                )
            return "No se encontraron resultados."
        except Exception as e:
            return f"Error en consulta q6: {str(e)}"

    def q7(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?politics ?pds ?mai ?bcr ?am
            WHERE {{
                ?tm a :Treatment_Manager_in_verification .
                ?tm :Protection_policies ?politics .
                ?tm :Personal_data_security_details ?pds .
                ?tm :Maintaining_the_accuracy_of_the_information ?mai .
                ?tm :Binding_cooperative_rules ?bcr .
                ?tm :Analysis_methodologies ?am .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return (
                # f"Responsable: {row.tm}\n"
                f"- Políticas de protección: {row.politics}\n"
                f"- Seguridad de datos personales: {row.pds}\n"
                f"- Mantenimiento de precisión: {row.mai}\n"
                f"- Reglas cooperativas vinculantes: {row.bcr}\n"
                f"- Metodologías de análisis: {row.am}"
            )
        return "No se encontraron resultados."

    def q8(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?sec
            WHERE {{
                ?tm a :Treatment_Manager_in_verification .
                ?rt a :Responsible_for_treatment_in_verification .
                ?tm :Personal_data_security_details ?sec .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return (
                # f"Encargado del tratamiento: {row.tm}\n"
                # f"Responsable del tratamiento: {row.rt}\n"
                f"{row.sec}"
            )
        return "No se encontraron resultados."

    def q9(self):
        return "Consulta q9 marcada como duplicada o errónea. Requiere revisión."

    def q10(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?exactitude
            WHERE {{
                ?rt a :Responsible_for_treatment_in_verification .
                ?rt :Maintaining_the_accuracy_of_the_information ?exactitude .
            }}
        """
        result = self.graph.query(query)
        respuestas = []
        for row in result:
            respuestas.append(f"{row.exactitude}")
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q11(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?riv
            WHERE {{
                ?h a :Holder_in_verification .
                ?h :Request_information_verification ?riv .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            return f"Solicitud de verificación: {row.riv}"
        return "No se encontraron resultados."

    def q12(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?slg ?sr ?vs
            WHERE {{
                ?tm a :Treatment_Manager_in_verification .
                ?tm :Slight ?slg .
                ?tm :Serious ?sr .
                ?tm :Very_serious ?vs .
            }}
            LIMIT 3
        """
        result = self.graph.query(query)
        resultados = []
        for row in result:
            resultados.append(
                f" Leve: {row.slg}, Grave: {row.sr}, Muy Grave: {row.vs}"
            )
        return "\n".join(resultados) if resultados else "No se encontraron resultados."

    def q13(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?law ?rg
            WHERE {{
                ?law :the_law_has_the_following_rights ?rg .
                ?rg a :Rights_in_verification .
                ?law a :Rights_in_verification .
            }}
        """
        try:
            result = self.graph.query(query)
            resultados = [f"Ley: {row.law}, Derecho: {row.rg}" for row in result]
            return "\n".join(resultados) if resultados else "No se encontraron resultados."
        except Exception as e:
            return f"Error en q13: {str(e)}"

    def q14(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?ivp ?pds ?pp ?am
            WHERE {{
                ?rt a :Responsible_for_treatment_in_verification .
                ?rt :Implementing_verification_processes ?ivp .
                ?rt :Personal_data_security_details ?pds .
                ?rt :Protection_policies ?pp .
                ?rt :Analysis_methodologies ?am .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return (
                # f"Responsable del tratamiento: {row.rt}\n"
                f"- Verificación: {row.ivp}\n"
                f"- Seguridad: {row.pds}\n"
                f"- Políticas: {row.pp}\n"
                f"- Metodologías: {row.am}"
            )
        return "No se encontraron resultados."

    def q15(self):
        return "Consulta q15 presenta errores. Requiere revisión del OWL."

    def q16(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?inf
            WHERE {{
                ?h a :Holder_in_verification .
                ?h :Informed ?inf .
            }}
        """
        result = self.graph.query(query)
        respuestas = []
        for row in result:
            respuestas.append(f" Informado: {row.inf}")
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q17(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT  ?cr
            WHERE {{
                ?pdpa a :Personal_Data_Protection_Authority_in_verification ;
                      :Correct ?cr .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            return f"{row.cr}"
        return "No se encontraron resultados."

    def q18(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?exp
            WHERE {{
                ?toc a :Transfer_or_communication ;
                     :Exceptions ?exp .
            }}
        """
        try:
            result = self.graph.query(query)
            return "\n".join(str(row.exp) for row in result) if result else "No se encontraron resultados."
        except Exception as e:
            return f"Error en q18: {str(e)}"

    def q19(self):
        return "Consulta q19 presenta errores. Requiere revisión de clases o propiedades."

    def q20(self):
        query = f"""
            PREFIX : <{ONTO_PREFIX}>
            SELECT ?cm
            WHERE {{
                ?bt :that_can_be_of_the_type ?cm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join(str(row.cm) for row in result) if result else "No se encontraron resultados."
    
    def q21(self):
        query = f"""
            PREFIX autogen1: <{DATOSPERSONALES_PREFIX}>
            SELECT ?d
            WHERE {{
              ?ra a autogen1:Right_of_access .
              ?ra autogen1:description ?d .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Descripción del derecho de acceso: {row.d}"
        return "No se encontraron resultados."

    def q22(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?wc
            WHERE {{
              ?pd a autogen0:Health_related_data_processing .
              ?pd autogen0:in_respect_to_the ?r .
              ?r <{DATOSPERSONALES_PREFIX}for_health-related_data_without_consent> ?wc .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            return f"Condición sin consentimiento: {row.wc}"
        return "No se encontraron resultados."

    def q23(self):
        query = f"""
        PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
        SELECT ?v
        WHERE {{
          ?cs a autogen0:Holder_between_15_to_17_years_old .
          ?cs autogen0:age ?v .
        }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f"Edad del titular: {row.v}" for row in result]) or "No se encontraron resultados."

    def q24(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
              ?cs a autogen0:Consent .
              ?cs autogen0:valid ?v .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {row.v}" for row in result]) or "No se encontraron resultados."


    def q25(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dl
            WHERE {{
              ?ra a autogen0:Right_of_access .
              ?ra autogen0:right_account_encumbered ?rae .
              ?rae autogen0:deadline_in_days_for_the_right_of_access ?dl .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Plazo en días para el derecho de acceso: {row.dl}"
        return "No se encontraron resultados."

    def q26(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?aco
            WHERE {{
              ?h a autogen0:Data_Owner .
              ?h autogen0:count_with_the_following ?cf .
              ?rs a autogen0:Rights .
              ?rs autogen0:are_constituted_of ?aco .
            }}
        """
        result = self.graph.query(query)
        respuestas = [f"Constituido por: {row.aco}" for row in result]
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q27(self):
        query = f"""
            PREFIX autogen1: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
              ?cs a autogen0:Right_to_information .
              ?cs autogen0:know_in_the_right_to_information ?v .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {row.v}" for row in result]) or "No se encontraron resultados."
       

    def q28(self):
        query = f"""
            PREFIX autogen1: <{DATOSPERSONALES_PREFIX}>
            SELECT ?arh
            WHERE {{
              ?dp a autogen1:Health_related_data_processing .
              ?dp autogen1:shall_be_authorized_by ?sba .
              ?sba autogen1:actions_regarding_health_data_processing ?arh .
            }}
        """
        result = self.graph.query(query)
        respuestas = [f"Acción autorizada: {row.arh}" for row in result]
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q29(self):
        return "Consulta q29 presenta errores. Revisión pendiente."

    def q30(self):
        query = f"""
            PREFIX autogen1: <{DATOSPERSONALES_PREFIX}>
            SELECT ?st
            WHERE {{
              ?dp a autogen1:Health_related_data_processing .
              ?dp autogen1:scenarios_for_treatment_by_private_and_public_entities ?st .
            }}
        """
        result = self.graph.query(query)
        for row in result:
            return f"Escenario: {row.st}"
        return "No se encontraron resultados."

    def q31(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?imi
            WHERE {{
              ?mi a autogen0:Minor_infractions .
              ?tm a autogen0:Data_Processor .
              ?mi autogen0:committed_by ?tm .
              ?tm autogen0:minor_infractions ?imi .
            }}
            LIMIT 4
        """
        result = self.graph.query(query)
        return "\n".join([f"Infracción leve: {row.imi}" for row in result]) or "No se encontraron resultados."

    def q32(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ib
            WHERE {{
              ?s a autogen0:Sanctions .
              ?s autogen0:will_be_imposed_by ?ib .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Impuesta por: {row.ib}"
        return "No se encontraron resultados."

    def q33(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?r
            WHERE {{
              ?apa a autogen0:Personal_data_protection_authority .
              ?apa autogen0:revocation ?r .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Revocación: {row.r}" for row in result]) or "No se encontraron resultados."

    def q34(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cd
            WHERE {{
              ?pda a autogen0:Personal_data_protection_authority .
              ?pda autogen0:duration_of_charge ?cd .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Duración del cargo: {row.cd}" for row in result]) or "No se encontraron resultados."

    def q35(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ina ?eci
            WHERE {{
              ?inn a autogen0:Inapplicability .
              ?inn autogen0:is_the_non_application_of_the_law_in ?ina .
              ?ina autogen0:explanation_of_concept_of_inapplicability ?eci .
            }}
        """
        result = self.graph.query(query)
        respuestas = [f"No aplicabilidad en: {row.ina}, Explicación: {row.eci}" for row in result]
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q36(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?aco
            WHERE {{
              ?dp a autogen0:Data_processing .
              ?dp autogen0:is_based_on ?ibo .
              ?ibo autogen0:are_composed_of ?aco .
            }}
        """
        result = self.graph.query(query)
        respuestas = [f"Compuesto por: {row.aco}" for row in result]
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q37(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?aco
            WHERE {{
              ?modp a autogen0:Members_of_the_personal_data_protection_system .
              ?modp autogen0:are_composed_of ?aco .
            }}
            LIMIT 6
        """
        result = self.graph.query(query)
        respuestas = [f"{row.aco}" for row in result]
        return "\n".join(respuestas) if respuestas else "No se encontraron resultados."

    def q38(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rae
            WHERE {{
              ?ra a autogen0:Right_of_access .
              ?ra autogen0:right_account_encumbered ?rae .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Obstáculo para el derecho de acceso: {row.rae}"
        return "No se encontraron resultados."

    def q39(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
            ?cs a autogen0:Anonymization .
            ?cs autogen0:description ?v . 
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Descripción de Anonymization: {row.v}"
        return "No se encontraron resultados."
    
    def q40(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
            ?cs a autogen0:Biometric_data .
            ?cs autogen0:description ?v . 
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Descripción de Biometric_data: {row.v}"
        return "No se encontraron resultados."
    def q41(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
            ?cs a autogen0:Certifying_entity .
            ?cs autogen0:description ?v . 
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Descripción de Certifying_entity: {row.v}"
        return "No se encontraron resultados."

    def q42(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?v
            WHERE {{
            ?cs a autogen0:Profile_making .
            ?cs autogen0:to_determine_behaviors_or_standards_relative_to ?v .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {row.v}" for row in result]) or "No se encontraron resultados."


