from rdflib import Graph
from config import RDF_PATH, DATOSPERSONALES_PREFIX

class QueryHandlerS:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = Graph()
            self.graph.parse(RDF_PATH, format="xml")
        else:
            self.graph = graph

    def s1(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT  ?exp
            WHERE {{
                ?in a autogen0:Inapplicability .
                ?in autogen0:is_the_non_application_of_the_law_in ?x .
                ?x autogen0:explanation_of_concept_of_inapplicability ?exp .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([str(row.exp) for row in result]) or "No se encontraron resultados."

    def s2(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT  ?esc
            WHERE {{
                ?t a autogen0:Territorial .
                ?t autogen0:the_law_applies_in ?apt .
                ?apt autogen0:territorial_application_scenario ?esc .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f"Escenario: {row.esc}" for row in result]) or "No se encontraron resultados."

    def s3(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?p
            WHERE {{
                ?int a autogen0:Members_of_the_personal_data_protection_system .
                ?int autogen0:are_composed_of ?p .
            }}
            LIMIT 6
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {str(row.p).split('#')[-1].replace('_', ' ').title()}" for row in result]) or "No se encontraron resultados."

    def s4(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT  ?d
            WHERE {{
                ?td a autogen0:Data_types .
                ?td autogen0:data_types_are_comprised_of ?cp .
                ?cp autogen0:description ?d .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.d}" for row in result]) or "No se encontraron resultados."

    def s5(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?x
            WHERE {{
                ?ec a autogen0:Certifying_entity .
                ?ec autogen0:is_authorized_by ?x .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([
            f"Autorizado por: {str(row.x).split('#')[-1].replace('_', ' ')}"
            for row in result
            ]) or "No se encontraron resultados."

    def s6(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tc
            WHERE {{
                ?fp a autogen0:Source_accessible_to_the_public .
                ?fp autogen0:has_the_characteristic_of_being ?tc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Característica: {row.tc}" for row in result]) or "No se encontraron resultados."

    def s7(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?x
            WHERE {{
                ?sc a autogen0:Personal_data_protection_seals .
                ?sc autogen0:is_given_by ?x .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Autorizado por: {str(row.x).split('#')[-1].replace('_', ' ')}"
            for row in result]) or "No se encontraron resultados."

    def s8(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?aa
            WHERE {{
                ?vs a autogen0:Personal_data_security_vulnerability .
                ?vs autogen0:affects_to ?aa .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Afecta a: {row.aa}" for row in result]) or "No se encontraron resultados."

    def s9(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT  ?r
            WHERE {{
                ?d a autogen0:Rights .
                ?d autogen0:responsible_for_channeling_the_exercise_of_rights ?r .
                ?d autogen0:responsible_for_channeling_the_exercise_of_rights ?dr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Responsables: {row.r}" for row in result]) or "No se encontraron resultados."

    def s10(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?desc
            WHERE {{
                ?d a autogen0:Rights .
                ?d autogen0:description_responsible_for_channeling_exercise_of_rights ?desc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Descripción: {row.desc}" for row in result]) or "No se encontraron resultados."
    
    def s11(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?lm
            WHERE {{
                ?d a autogen0:Rights .
                ?d autogen0:limitation_on_exercise_of_rights_by_secondary_laws ?lm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Limitación por leyes secundarias: {row.lm}" for row in result]) or "No se encontraron resultados."

    def s12(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tl
            WHERE {{
                {{
                    ?t a autogen0:Data_processing .
                    ?t autogen0:conditions_for_legitimate_treatment ?tl .
                }}
                UNION
                {{
                    ?c a autogen0:Consent .
                    ?c autogen0:conditions_for_legitimate_treatment ?tl .
                }}
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {row.tl}" for row in result]) or "No se encontraron resultados."

    def s13(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ds
            WHERE {{
                ?il a autogen0:Legal_interest .
                ?il autogen0:description ?ds .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f"Descripción del interés legal: {row.ds}"
        return "No se encontraron resultados."

    def s14(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ptc
            WHERE {{
                ?c a autogen0:Consent .
                ?c autogen0:to_deal_with_and_communicate_personal_data_must ?ptc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Para comunicar datos: {row.ptc}" for row in result]) or "No se encontraron resultados."

    def s15(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cv
            WHERE {{
                ?c a autogen0:Consent .
                ?c autogen0:valid ?cv .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f"{row.cv}" for row in result]) or "No se encontraron resultados."

    def s16(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ds
            WHERE {{
                ?vc a autogen0:Consent_defects .
                ?vc autogen0:description ?ds .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        for row in result:
            return f" {row.ds}"
        return "No se encontraron resultados."

    def s17(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cr
            WHERE {{
                ?c rdf:type autogen0:Revocation_of_consent  .
                ?c autogen0:when_it_can_be_produced ?cr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Se puede producir: {row.cr}" for row in result]) or "No se encontraron resultados."

    def s18(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?j
            WHERE {{
                ?c a autogen0:Revocation_of_consent .
                ?c autogen0:justification_for_revocation ?j .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Justificación para revocación: {row.j}" for row in result]) or "No se encontraron resultados."

    def s19(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cds
            WHERE {{
                ?mr a autogen0:Recall_mechanisms .
                ?mr autogen0:must_guarantee ?cds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"{row.cds}" for row in result]) or "No se encontraron resultados."

    def s20(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cds
            WHERE {{
                ?mr a autogen0:Recall_mechanisms .
                ?mr autogen0:must_be ?cds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Debe ser: {row.cds}" for row in result]) or "No se encontraron resultados."
    
    def s21(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?e
            WHERE {{
              ?mr a autogen0:Recall_mechanisms .
              ?mr autogen0:son_establecidos_por ?e .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Autorizado por: {str(row.e).split('#')[-1].replace('_', ' ')}"
            for row in result]) or "No se encontraron resultados."

    def s22(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tarc
            WHERE {{
              ?rc a autogen0:Revocation_of_consent .
              ?rc autogen0:regarding_treatment ?rt .
              ?rt autogen0:before_the_revocation_of_consent_is_considered_to_be_considered ?tarc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"Antes de revocar se considera: {row.tarc}" for row in result]) or "No se encontraron resultados."

    def s23(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tbil
            WHERE {{
              ?td a autogen0:Data_processing .
              ?td autogen0:low_legitimate_interest ?tbil .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.tbil}" for row in result]) or "No se encontraron resultados."

    def s24(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?fds
            WHERE {{
              ?f a autogen0:Purpose .
              ?f autogen0:shall_be ?fds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"{row.fds}" for row in result]) or "No se encontraron resultados."

    def s25(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tdf
            WHERE {{
              ?f a autogen0:Purpose .
              ?f autogen0:is_distinct_from_data_collection_in_the ?df .
              ?df autogen0:for_different_purpose ?tdf .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.tdf}" for row in result]) or "No se encontraron resultados."

    def s26(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dct
            WHERE {{
              ?f a autogen0:Purpose .
              ?f autogen0:is_distinct_from_data_collection_in_the ?df .
              ?df autogen0:determine_the_compatibility ?dct .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.dct}" for row in result]) or "No se encontraron resultados."

    def s27(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cc
            WHERE {{
              ?c a autogen0:Quality .
              ?c autogen0:associated_to ?td .
              ?td autogen0:to_comply_with_quality_you_must ?cc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"{row.cc}" for row in result]) or "No se encontraron resultados."

    def s28(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ec
            WHERE {{
            ?c a autogen0:Quality .
            ?c autogen0:is_in_charge_of ?ec .
            }}
        """  # <-- cierre faltante

        result = self.graph.query(query)

        if result:
            return "\n".join([
                f"Autorizado por: {str(row.ec).split('#')[-1].replace('_', ' ')}"
                for row in result
            ])
        else:
            return "No se encontraron resultados."


    def s29(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?nii
            WHERE {{
              ?dp a autogen0:Personal_data .
              ?dp autogen0:it_is_not_imputable_to_be_inaccurate_when ?nii .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"No imputable cuando: {row.nii}" for row in result]) or "No se encontraron resultados."

    def s30(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cesr
            WHERE {{
              ?c a autogen0:Conservation .
              ?c autogen0:responsible_for_establishing_the_deadlines_for_suspension_or_periodic_review_within_data_processing_is ?cesr .
            }}
        """
        result = self.graph.query(query)
        if result:
            return "\n".join([
                f"Autorizado por: {str(row.cesr).split('#')[-1].replace('_', ' ')}"
                for row in result
            ])
        else:
            return "No se encontraron resultados."

    def s31(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?catdp
            WHERE {{
              ?c a autogen0:Conservation .
              ?c autogen0:extended_preservation_of_personal_data_processing ?catdp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.catdp}" for row in result]) or "No se encontraron resultados."

    def s32(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tdm
            WHERE {{
              ?s a autogen0:Security .
              ?s autogen0:types_of_safety_measures ?tdm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"{row.tdm}" for row in result]) or "No se encontraron resultados."

    def s33(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eims
            WHERE {{
              ?s a autogen0:Security .
              ?s autogen0:responsible_for_implementing_safety_measures ?eims .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f"Miembro: {str(row.eims).split('#')[-1].replace('_', ' ').title()}" for row in result]) or "No se encontraron resultados."

    def s34(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?arpd
            WHERE {{
              ?r a autogen0:Data_Controller .
              ?r autogen0:activity_in_respect_to_proactive_and_demonstrated_responsibility ?arpd .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.arpd}" for row in result]) or "No se encontraron resultados."

    def s35(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dhacrrp
            WHERE {{
              ?r a autogen0:Data_Controller .
              ?r autogen0:must_have_been_complied_with_regard_to_proactive_responsibility ?dhacrrp .
            }}
        """
        result = self.graph.query(query)
        return "\n\n".join([f" {str(row.dhacrrp).split('#')[-1].replace('_', ' ').title()}" for row in result]) or "No se encontraron resultados."


    def s36(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?acm
            WHERE {{
              ?r a autogen0:Data_Controller .
              ?r autogen0:accrediting_compliance_with_the_mechanisms ?acm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.acm}" for row in result]) or "No se encontraron resultados."

    def s37(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rcc
            WHERE {{
            ?r a autogen0:Data_Controller .
            ?r autogen0:must_render_accounts_regarding_the_treatment_with ?rcc .
            }}
        """
        result = self.graph.query(query)

        if result:
            return "\n\n".join([
                f"{str(row.rcc).split('#')[-1].replace('_', ' ').title()}"
                for row in result
            ])
        else:
            return "No se encontraron resultados."



    def s38(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ics
            WHERE {{
              ?ic a autogen0:Independence_of_control .
              ?ic autogen0:is_supervised_by ?ics .
            }}
        """
        result = self.graph.query(query)
        if result:
            return "\n\n".join([
                f"{str(row.ics).split('#')[-1].replace('_', ' ').title()}"
                for row in result
            ])
        else:
            return "No se encontraron resultados."


    def s39(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?aric
            WHERE {{
              ?ic a autogen0:Independence_of_control .
              ?ic autogen0:is_supervised_by ?ics .
              ?ics autogen0:actions_regarding_independence_of_control ?aric .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.aric}" for row in result]) or "No se encontraron resultados."

    def s40(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?trne
            WHERE {{
              ?dpme a autogen0:Specialized_subject_data .
              ?dpme autogen0:regulated_treatment_in_specialized_regulations_regarding ?trne .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.trne}" for row in result]) or "No se encontraron resultados."

    def s41(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?es
            WHERE {{
              ?dme a autogen0:Specialized_subject_data .
              ?dme autogen0:will_be_subject_to ?es .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.es}" for row in result]) or "No se encontraron resultados."

    def s42(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dcm ?d
            WHERE {{
               ?dme rdf:type autogen0:Minimum_criteria .
                ?dme autogen0:are_composed_of ?dcm .
                ?dcm autogen0:description ?d .
            }}
            LIMIT 3
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.dcm.split('#')[-1]}, Descripción: {row.d}" for row in result]) or "No se encontraron resultados."

    def s43(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ddc
            WHERE {{
              ?di a autogen0:Right_to_information .
              ?di autogen0:know_in_the_right_to_information ?ddc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"  {row.ddc}" for row in result]) or "No se encontraron resultados."

    def s44(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?odpdt
            WHERE {{
              ?c a autogen0:Consent .
              ?c autogen0:in_cases_of_direct_data_gathering_by_the ?codt .
              ?codt autogen0:obtaining_personal_data_directly_by_the_owner ?odpdt .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"{row.odpdt}" for row in result]) or "No se encontraron resultados."

    def s45(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dcm 
            WHERE {{
              ?dme rdf:type autogen0:Data_Owner .
              ?dme autogen0:in_case_of_no_direct_obtaining_by_the_owner ?dcm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"   {row.dcm}" for row in result]) or "No se encontraron resultados."

    def s46(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?m
            WHERE {{
              ?c a autogen0:Consent .
              ?c autogen0:how_the_information_may_be_transmitted_to_the_owner ?m .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f"   {row.m}" for row in result]) or "No se encontraron resultados."

    def s47(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cdti
            WHERE {{
              ?c a autogen0:Consent .
              ?c autogen0:characteristics_that_the_information_transferred_to_the_owner_must_have ?cdti .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.cdti}" for row in result]) or "No se encontraron resultados."

    def s48(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dce
            WHERE {{
              ?da a autogen0:Right_of_access .
              ?da autogen0:right_account_encumbered ?dce .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        if result:
            return "\n\n".join([
                f"{str(row.dce).split('#')[-1].replace('_', ' ').title()}"
                for row in result
            ])
        else:
            return "No se encontraron resultados."

    def s49(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ada
            WHERE {{
              ?da a autogen0:Right_of_access .
              ?da autogen0:right_account_encumbered ?dce .
              ?dce autogen0:activity_within_right_of_access ?ada .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([f" {row.ada}" for row in result]) or "No se encontraron resultados."

    def s50(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pad
            WHERE {{
              ?da a autogen0:Right_of_access .
              ?da autogen0:right_account_encumbered ?dce .
              ?dce autogen0:deadline_in_days_for_the_right_of_access ?pad .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([f"   {row.pad}" for row in result]) or "No se encontraron resultados."
