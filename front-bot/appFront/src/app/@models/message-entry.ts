export interface MessageEntry{
    id: string;
    content: string;
    role: 'user' | 'assistant';
    createdAd: Date;
}

export interface ChatEntry {
  mensaje: string;
  respuesta: string;
}

export interface ChatHistorico {
  id_user: number;
  email: string;
  chatLog: ChatEntry[];
}

export interface ConsultaHistoricoDetalle {
  detalle_id: number;
  id_chathistorico: number;
  historial: string;
  fecha: string;
  id_user: number;
  email: string;
}