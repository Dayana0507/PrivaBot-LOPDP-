from rdflib import Graph
from config import RDF_PATH, DATOSPERSONALES_PREFIX

class QueryHandlerT:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = Graph()
            self.graph.parse(RDF_PATH, format="xml")
        else:
            self.graph = graph

    def t51(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dce
            WHERE {{
                ?dra a autogen0:Right_to_correction_and_update .
                ?dra autogen0:right_account_encumbered ?dce .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dce) for row in result]) or "No se encontraron resultados."

    def t52(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?adra
            WHERE {{
                ?dra a autogen0:Right_to_correction_and_update .
                ?dra autogen0:right_account_encumbered ?dce .
                ?dce autogen0:activity_within_the_right_of_correction_and_update ?adra .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.adra) for row in result]) or "No se encontraron resultados."

    def t53(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?p
            WHERE {{
                ?dra a autogen0:Right_to_correction_and_update .
                ?dra autogen0:right_account_encumbered ?dce .
                ?dce autogen0:time_of_attention_within_days_for_the_right_of_correction_and_update ?p .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.p) for row in result]) or "No se encontraron resultados."

    def t54(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dce
            WHERE {{
                ?de a autogen0:Right_of_deletion .
                ?de autogen0:right_account_encumbered ?dce .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dce) for row in result]) or "No se encontraron resultados."

    def t55(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cedp
            WHERE {{
                ?de a autogen0:Right_of_deletion .
                ?de autogen0:when_personal_data_may_be_deleted ?cedp .
            }}
            LIMIT 7
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cedp) for row in result]) or "No se encontraron resultados."

    def t56(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ade
            WHERE {{
                ?de a autogen0:Right_of_deletion .
                ?de autogen0:right_account_encumbered ?dce .
                ?dce autogen0:activity_within_the_right_of_deletion ?ade .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ade) for row in result]) or "No se encontraron resultados."

    def t57(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pde
            WHERE {{
                ?de a autogen0:Right_of_deletion .
                ?de autogen0:right_account_encumbered ?dce .
                ?dce autogen0:time_of_attention_in_days_for_the_right_of_removal ?pde .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pde) for row in result]) or "No se encontraron resultados."

    def t58(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dce
            WHERE {{
                ?do a autogen0:Right_of_opposition .
                ?do autogen0:right_account_encumbered ?dce .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dce) for row in result]) or "No se encontraron resultados."

    def t59(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cpot
            WHERE {{
                ?do a autogen0:Right_of_opposition .
                ?do autogen0:when_it_can_be_opposed_to_treatment ?cpot .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cpot) for row in result]) or "No se encontraron resultados."

    def t60(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?md
            WHERE {{
                ?do a autogen0:Right_of_opposition .
                ?do autogen0:in_direct_marketing_cases ?md .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.md) for row in result]) or "No se encontraron resultados."

    def t61(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ado
            WHERE {{
                ?do a autogen0:Right_of_opposition .
                ?do autogen0:right_account_encumbered ?dce .
                ?dce autogen0:activity_within_opposition_law ?ado .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ado) for row in result]) or "No se encontraron resultados."

    def t62(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pado
            WHERE {{
                ?do a autogen0:Right_of_opposition .
                ?do autogen0:right_account_encumbered ?dce .
                ?dce autogen0:deadline_in_days_for_the_right_to_oppose_opposition ?pado .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pado) for row in result]) or "No se encontraron resultados."

    def t63(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?edc
            WHERE {{
                ?ed a autogen0:Exceptions_of_rights .
                ?ed autogen0:rights_to_correct_update_update_delete_and_oppose ?edc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.edc) for row in result]) or "No se encontraron resultados."

    def t64(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cst
            WHERE {{
                ?dst a autogen0:Right_to_suspension_of_treatment .
                ?dst autogen0:conditions_for_the_suspension_of_treatment ?cst .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cst) for row in result]) or "No se encontraron resultados."

    def t65(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?st
            WHERE {{
                ?t a autogen0:Data_Owner .
                ?t autogen0:in_case_of_suspension_of_treatment_must_resort_to ?st .
            }}
        """
        result = self.graph.query(query)

        if result:
            return "\n\n".join([
                str(row.st).split('#')[-1].replace('_', ' ').title()
                for row in result
            ])
        else:
            return "No se encontraron resultados."


    def t66(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?st
            WHERE {{
                ?t a autogen0:Right_to_suspension_of_treatment  .
                ?t autogen0:incurring_the_owner_to_the_personal_data_protection_authority ?st .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.st) for row in result]) or "No se encontraron resultados."

    def t67(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?idp
            WHERE {{
                ?t a autogen0:Data_Owner .
                ?t autogen0:in_case_of_impugning_the_exaccuracy_of_data_a ?tcidp .
                ?tcidp autogen0:in_the_event_of_a_challenge_of_data_exaccuracy ?idp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.idp) for row in result]) or "No se encontraron resultados."

    def t68(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?stdcidp
            WHERE {{
                ?dst a autogen0:Right_to_suspension_of_treatment .
                ?dst autogen0:assumptions_for_processing_the_data_in_the_event_of_a_data_challenge ?stdcidp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.stdcidp) for row in result]) or "No se encontraron resultados."

    def t69(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cda
            WHERE {{
                ?t a autogen0:Data_Owner .
                ?dnva a autogen0:Right_not_to_be_object_to_automated_evaluations .
                ?dnva autogen0:for_the ?t .
                ?t autogen0:in_cases_of_automated_evaluations ?cda .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cda) for row in result]) or "No se encontraron resultados."

    def t70(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?edva
            WHERE {{
                ?ed a autogen0:Exceptions_of_rights .
                ?ed autogen0:rights_to_not_be_the_object_of_automated_assessments ?edva .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.edva) for row in result]) or "No se encontraron resultados."
    
    def t71(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rdova
            WHERE {{
                ?ed a autogen0:Exceptions_of_rights .
                ?ed autogen0:the_right_to_not_be_object_to_automated_assessments_may_not_be_revocable ?rdova .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.rdova) for row in result]) or "No se encontraron resultados."

    def t72(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dnst
            WHERE {{
                ?dova a autogen0:Right_not_to_be_object_to_automated_evaluations .
                ?dova autogen0:will_not_be_able_to_deal ?ntd .
                ?ntd autogen0:data_not_subject_to_processing_according_to_the_right_to_not_be_the_object_of_automated_decisions ?dnst .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dnst) for row in result]) or "No se encontraron resultados."

    def t73(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dst
            WHERE {{
                ?dova a autogen0:Right_not_to_be_object_to_automated_evaluations .
                ?dova autogen0:will_not_be_able_to_deal ?ntd .
                ?ntd autogen0:data_subjects_to_treatment_according_to_the_right_to_not_be_the_object_of_automated_decisions ?dst .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dst) for row in result]) or "No se encontraron resultados."

    def t74(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?t
            WHERE {{
                ?t a autogen0:Data_Owner .
                ?t autogen0:can_give_explicit_consent_to_treatment true .
            }}
        """
        result = self.graph.query(query)

        if result:
            return "\n".join([
                str(row.t).split("#")[-1].replace("_", " ").title()
                for row in result
            ])
        else:
            return "No se encontraron resultados."


    def t75(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?gq
            WHERE {{
                ?dc a autogen0:Right_to_consult .
                ?dc autogen0:garatize_that ?gq .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.gq) for row in result]) or "No se encontraron resultados."

    def t76(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dpc
            WHERE {{
                ?dc a autogen0:Right_to_consult .
                ?dc autogen0:where_you_can_consult ?dpc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dpc) for row in result]) or "No se encontraron resultados."

    def t77(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?sdad
            WHERE {{
                ?ded a autogen0:Right_to_digital_education .
                ?ded autogen0:right_to_access_and_availability ?sdad .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.sdad) for row in result]) or "No se encontraron resultados."

    def t78(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dged
            WHERE {{
                ?ded a autogen0:Right_to_digital_education .
                ?ded autogen0:guaranteeing_digital_education ?dged .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dged) for row in result]) or "No se encontraron resultados."

    def t79(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cied
            WHERE {{
                ?ded a autogen0:Right_to_digital_education .
                ?ded autogen0:inclusiveness_in ?cied .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cied) for row in result]) or "No se encontraron resultados."

    def t80(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?d
            WHERE {{
                ?ed a autogen0:Exercise_of_rights .
                ?ed autogen0:description ?d .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.d) for row in result]) or "No se encontraron resultados."
    
    def t81(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ddc
            WHERE {{
                ?ed a autogen0:Exercise_of_rights .
                ?ed autogen0:must_provide_training_and_information ?ddc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ddc) for row in result]) or "No se encontraron resultados."

    def t82(self):
            query = f"""
                PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
                SELECT ?ecp
                WHERE {{
                    ?cde a autogen0:Special_personal_data_categories .
                    ?cde autogen0:special_categories_of_personal_data_are_composed_of ?ecp .
                }}
                LIMIT 4
            """
            result = self.graph.query(query)

            if result:
                return "\n".join([
                    str(row.ecp).split("#")[-1].replace("_", " ").title()
                    for row in result
                ])
            else:
                return "No se encontraron resultados."


    def t83(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?etds
            WHERE {{
                ?tds a autogen0:Sensitive_data_processing .
                ?tds autogen0:sensitive_data_processing_scenarios ?etds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.etds) for row in result]) or "No se encontraron resultados."

    def t84(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cu
            WHERE {{
                ?tf a autogen0:Deceased_owner .
                ?tf autogen0:account_with_a ?cu .
            }}
        """
        result = self.graph.query(query)

        if result:
            return "\n".join([
                str(row.cu).split("#")[-1].replace("_", " ").title()
                for row in result
            ])
        else:
            return "No se encontraron resultados."


    def t85(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ed
            WHERE {{
                ?tf a autogen0:Deceased_owner .
                ?tf autogen0:account_with_a ?cu .
                ?cu autogen0:exercise_of_rights_by_the_deceased_owner ?ed .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ed) for row in result]) or "No se encontraron resultados."

    def t86(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pe
            WHERE {{
                ?tdc a autogen0:Credit_data_processing .
                ?tdc autogen0:allow_evaluate ?pe .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pe) for row in result]) or "No se encontraron resultados."

    def t87(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pis
            WHERE {{
                ?tdc a autogen0:Credit_data_processing .
                ?tdc autogen0:for_information_about ?pis .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pis) for row in result]) or "No se encontraron resultados."

    def t88(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?fdo
            WHERE {{
                ?tdc a autogen0:Credit_data_processing .
                ?tdc autogen0:sources_from_whence_the_credit_data_was_obtained ?fdo .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.fdo) for row in result]) or "No se encontraron resultados."

    def t89(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tddc
            WHERE {{
                ?tdc a autogen0:Credit_data_processing .
                ?tdc autogen0:destined ?tddc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tddc) for row in result]) or "No se encontraron resultados."

    def t90(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?npad
            WHERE {{
                ?tdc a autogen0:Credit_data_processing .
                ?tdc autogen0:cannot_be_done_with_the_processing_of_credit_data ?npad .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.npad) for row in result]) or "No se encontraron resultados."

    def t91(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dtd
            WHERE {{
                ?dtdc a autogen0:Rights_of_credit_data_owners .
                ?dtdc autogen0:rights_of_credit_data_holders ?dtd .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dtd) for row in result]) or "No se encontraron resultados."

    def t92(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dadp
            WHERE {{
                ?dtdc a autogen0:Rights_of_credit_data_owners .
                ?dtdc autogen0:right_to_access_by_credit_data_holders ?dadp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dadp) for row in result]) or "No se encontraron resultados."

    def t93(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?mada
            WHERE {{
                ?dtdc a autogen0:Rights_of_credit_data_owners .
                ?dtdc autogen0:mechanisms_to_secure_the_right_of_access_of_the_credit_data_holder ?mada .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.mada) for row in result]) or "No se encontraron resultados."

    def t94(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?daredc
            WHERE {{
                ?dtdc a autogen0:Rights_of_credit_data_owners .
                ?dtdc autogen0:right_to_update_correction_or_deletion_of_the_credit_data_holder ?daredc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.daredc) for row in result]) or "No se encontraron resultados."

    def t95(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?afi
            WHERE {{
                ?dtdc a autogen0:Rights_of_credit_data_owners .
                ?dtdc autogen0:source_of_information_activity_on_the_application ?afi .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.afi) for row in result]) or "No se encontraron resultados."

    def t96(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rtdrs
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:health-related_data_collection_and_processing ?rtdrs .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.rtdrs) for row in result]) or "No se encontraron resultados."

    def t97(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cdrs
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:in_respect_to_the ?ctds .
                ?ctds autogen0:for_health-related_data_without_consent ?cdrs .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cdrs) for row in result]) or "No se encontraron resultados."

    def t98(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eatds
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:application_scenarios_for_processing_of_data_without_consent ?eatds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.eatds) for row in result]) or "No se encontraron resultados."

    def t99(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dst
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:supervise_treatment_in_health_service_management_activities ?dst .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dst) for row in result]) or "No se encontraron resultados."

    def t100(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tdrsdsa
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:shall_be_authorized_by ?tdrsdsa .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tdrsdsa) for row in result]) or "No se encontraron resultados."
