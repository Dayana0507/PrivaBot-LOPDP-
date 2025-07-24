from rdflib import Graph
from config import RDF_PATH, DATOSPERSONALES_PREFIX

class QueryHandlerU:
    def __init__(self, graph=None):
        if graph is None:
            self.graph = Graph()
            self.graph.parse(RDF_PATH, format="xml")
        else:
            self.graph = graph

    def u101(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?artds
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:shall_be_authorized_by ?tdrsdsa .
                ?tdrsdsa autogen0:actions_regarding_health_data_processing ?artds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.artds) for row in result]) or "No se encontraron resultados."

    def u102(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?atds
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:authorization_for_treatment_of_anonymized_health_data ?atds .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.atds) for row in result]) or "No se encontraron resultados."

    def u103(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tdepp
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:purposes_of_the_processing_of_data_by_private_and_public_entities ?tdepp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tdepp) for row in result]) or "No se encontraron resultados."

    def u104(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tdepp
            WHERE {{
                ?tds a autogen0:Health_related_data_processing .
                ?tds autogen0:scenarios_for_treatment_by_private_and_public_entities ?tdepp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tdepp) for row in result]) or "No se encontraron resultados."

    def u105(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?o
            WHERE {{
                ?rt a autogen0:Data_Controller .
                ?rt autogen0:obligations ?o .
            }}
            LIMIT 16
        """
        result = self.graph.query(query)
        return "\n".join([str(row.o) for row in result]) or "No se encontraron resultados."

    def u106(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?adpd
            WHERE {{
                ?dpd a autogen0:Delegate .
                ?dpd autogen0:a_data_protection_delegate_will_be_assigned ?adpd .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.adpd) for row in result]) or "No se encontraron resultados."

    def u107(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?fdd
            WHERE {{
                ?dpd a autogen0:Delegate .
                ?dpd autogen0:control_functions ?fdd .
            }}
            LIMIT 5
        """
        result = self.graph.query(query)
        return "\n".join([str(row.fdd) for row in result]) or "No se encontraron resultados."

    def u108(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dop
            WHERE {{
                ?dpd a autogen0:Delegate .
                ?dpd autogen0:shall_be_observed_by ?dop .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dop) for row in result]) or "No se encontraron resultados."

    def u109(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?odd
            WHERE {{
                ?dpd a autogen0:Delegate .
                ?dpd autogen0:shall_be_observed_by ?dop .
                ?dop autogen0:delegate_comments ?odd .
            }}
            LIMIT 5
        """
        result = self.graph.query(query)
        return "\n".join([str(row.odd) for row in result]) or "No se encontraron resultados."

    def u110(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pshp
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:may_be_made_by ?pshp .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pshp) for row in result]) or "No se encontraron resultados."

    def u111(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rvdh
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:are_destined_to ?rvdh .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.rvdh) for row in result]) or "No se encontraron resultados."

    def u112(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?psh
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:may_be_made_in_shape ?psh .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.psh) for row in result]) or "No se encontraron resultados."

    def u113(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pshpm
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:may_be_done_by_means ?pshpm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pshpm) for row in result]) or "No se encontraron resultados."

    def u114(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rd
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:claims_of ?rd .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.rd) for row in result]) or "No se encontraron resultados."

    def u115(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?pecr
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:submit_in_case_of_claim ?pecr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.pecr) for row in result]) or "No se encontraron resultados."

    def u116(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cr
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:answer_the_claim ?cr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cr) for row in result]) or "No se encontraron resultados."

    def u117(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?acr
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:before_answering_the_claim ?acr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.acr) for row in result]) or "No se encontraron resultados."

    def u118(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?annr
            WHERE {{
                ?r a autogen0:Claims .
                ?r autogen0:in_the_face_of_a_denial_or_no_response_to_the_claim ?annr .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.annr) for row in result]) or "No se encontraron resultados."

    def u119(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ecimc
            WHERE {{
                ?mc autogen0:in_the_case_of_non-compliance_of ?ecimc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ecimc) for row in result]) or "No se encontraron resultados."

    def u120(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?mcsip
            WHERE {{
                ?mc autogen0:will_be_imposed_by ?mcsip .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.mcsip) for row in result]) or "No se encontraron resultados."

    def u121(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cmc
            WHERE {{
                ?mc autogen0:what_will_be_the_corrective_measures ?cmc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cmc) for row in result]) or "No se encontraron resultados."

    def u122(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?admc
            WHERE {{
                ?mc autogen0:before_dictating_corrective_measures ?admc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.admc) for row in result]) or "No se encontraron resultados."

    def u123(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cimc
            WHERE {{
                ?mc autogen0:cases_to_incur_in_corrective_measures ?cimc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cimc) for row in result]) or "No se encontraron resultados."

    def u124(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?mcil
            WHERE {{
                ?mc autogen0:for_minor_infractions ?mcil .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.mcil) for row in result]) or "No se encontraron resultados."

    def u125(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?mcig
            WHERE {{
                ?mc autogen0:for_serious_infractions ?mcig .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.mcig) for row in result]) or "No se encontraron resultados."

    def u126(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?mcimg
            WHERE {{
                ?mc autogen0:for_very_serious_offenses ?mcimg .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.mcimg) for row in result]) or "No se encontraron resultados."

    def u127(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eil
            WHERE {{
                ?il a autogen0:Minor_infractions .
                ?il autogen0:committed_by ?rt .
                ?rt a autogen0:Data_Controller .
                ?rt autogen0:minor_infractions ?eil .
            }}
            LIMIT 5
        """
        result = self.graph.query(query)
        return "\n".join([str(row.eil) for row in result]) or "No se encontraron resultados."

    def u128(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eig
            WHERE {{
                ?rt a autogen0:Data_Controller .
                ?rt autogen0:serious_infractions ?eig .
                ?ig a autogen0:Serious_infractions .
                ?ig autogen0:committed_by ?rt .
            }}
            LIMIT 14
        """
        result = self.graph.query(query)
        return "\n".join([str(row.eig) for row in result]) or "No se encontraron resultados."

    def u129(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eil
            WHERE {{
                ?il a autogen0:Minor_infractions .
                ?il autogen0:committed_by ?et .
                ?et autogen0:minor_infractions ?eil .
                ?et a autogen0:Data_Processor .
            }}
            LIMIT 4
        """
        result = self.graph.query(query)
        return "\n".join([str(row.eil) for row in result]) or "No se encontraron resultados."

    def u130(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?eig
            WHERE {{
                ?ig a autogen0:Serious_infractions .
                ?ig autogen0:committed_by ?et .
                ?et a autogen0:Data_Processor .
                ?et autogen0:serious_infractions ?eig .
            }}
            LIMIT 8
        """
        result = self.graph.query(query)
        return "\n".join([str(row.eig) for row in result]) or "No se encontraron resultados."

    def u131(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?ec
            WHERE {{
                ?s a autogen0:Sanctions .
                ?s autogen0:are_made_of ?ec .
            }}
            LIMIT 2
        """
        result = self.graph.query(query)
        return "\n".join([str(row.ec) for row in result]) or "No se encontraron resultados."

    def u132(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?si
            WHERE {{
                ?s a autogen0:Sanctions .
                ?s autogen0:will_be_imposed_by ?si .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.si) for row in result]) or "No se encontraron resultados."

    def u133(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?d
            WHERE {{
                ?sil a autogen0:Minor_infractions_penalties .
                ?sil autogen0:destined_for ?d .
            }}
            LIMIT 2
        """
        result = self.graph.query(query)
        return "\n".join([str(row.d) for row in result]) or "No se encontraron resultados."

    def u134(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tssf
            WHERE {{
                ?sil a autogen0:Minor_infractions_penalties .
                ?sil autogen0:type_of_penalty_for_infractions_toward_public_servants_or_officials ?tssf .
            }}
            LIMIT 2
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tssf) for row in result]) or "No se encontraron resultados."

    def u135(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tssf
            WHERE {{
                ?sil a autogen0:Minor_infractions_penalties .
                ?sil autogen0:type_of_penalty_for_infractions_to_the_responsible_party_or_the_processor ?tssf .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tssf) for row in result]) or "No se encontraron resultados."

    def u136(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dm
            WHERE {{
                ?sil a autogen0:Minor_infractions_penalties .
                ?sil autogen0:determination_of_the_fine_in_respect_to_penalties_for_infringement_of_the_responsible_person_or_person_in_charge_of_treatment ?dm .
            }}
            LIMIT 4
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dm) for row in result]) or "No se encontraron resultados."

    def u137(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?d
            WHERE {{
                ?sig a autogen0:Penalties_for_Serious_Infringements .
                ?sig autogen0:destined_for ?d .
            }}
            LIMIT 2
        """
        result = self.graph.query(query)
        return "\n".join([str(row.d) for row in result]) or "No se encontraron resultados."

    def u138(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tssf
            WHERE {{
                ?sig a autogen0:Penalties_for_Serious_Infringements .
                ?sig autogen0:type_of_penalty_for_infractions_toward_public_servants_or_officials ?tssf .
            }}
            LIMIT 2
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tssf) for row in result]) or "No se encontraron resultados."

    def u139(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?tsret
            WHERE {{
                ?sig a autogen0:Penalties_for_Serious_Infringements .
                ?sig autogen0:type_of_penalty_for_infractions_to_the_responsible_party_or_the_processor ?tsret .
            }}
            LIMIT 1
        """
        result = self.graph.query(query)
        return "\n".join([str(row.tsret) for row in result]) or "No se encontraron resultados."

    def u140(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dm
            WHERE {{
                ?sig a autogen0:Penalties_for_Serious_Infringements .
                ?sig autogen0:determination_of_the_fine_in_respect_to_penalties_for_infringement_of_the_responsible_person_or_person_in_charge_of_treatment ?dm .
            }}
            LIMIT 4
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dm) for row in result]) or "No se encontraron resultados."
    
    def u141(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?f
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:functions ?f .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.f) for row in result]) or "No se encontraron resultados."

    def u142(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?cm
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:known_as ?cm .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.cm) for row in result]) or "No se encontraron resultados."

    def u143(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?d
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:designation ?d .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.d) for row in result]) or "No se encontraron resultados."

    def u144(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?rdc
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:requirements_that_must_be_met ?rdc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.rdc) for row in result]) or "No se encontraron resultados."

    def u145(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?dc
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:duration_of_charge ?dc .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.dc) for row in result]) or "No se encontraron resultados."

    def u146(self):
        query = f"""
            PREFIX autogen0: <{DATOSPERSONALES_PREFIX}>
            SELECT ?r
            WHERE {{
                ?apd a autogen0:Personal_data_protection_authority .
                ?apd autogen0:revocation ?r .
            }}
        """
        result = self.graph.query(query)
        return "\n".join([str(row.r) for row in result]) or "No se encontraron resultados."

