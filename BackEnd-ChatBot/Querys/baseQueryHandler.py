class BaseQueryHandler:
    def __init__(self, graph):
        self.graph = graph

    def run_query(self, query, format_func=None):
        try:
            result = self.graph.query(query)
            if not result:
                return "No se encontraron resultados."
            if format_func:
                return format_func(result)
            return "\n".join([", ".join([str(col) for col in row]) for row in result])
        except Exception as e:
            return f"Error al ejecutar consulta: {str(e)}"
