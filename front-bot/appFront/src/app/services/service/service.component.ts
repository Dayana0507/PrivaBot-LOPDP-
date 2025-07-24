// import { Component, Injectable } from '@angular/core';
// import { identity, Observable, of } from 'rxjs';
// import { MessageEntry } from '../../@models/message-entry';

// @Injectable({
//   providedIn:'root'
// })

// export class ServiceComponent {
//   public  sendMessage (message:MessageEntry): Observable<MessageEntry>{
//     return of({
//       id: crypto.randomUUID(),
//     content: 'hola, Mensaje de service.component',
//     role: 'assistant',
//     createdAd: new Date()
//     });
//   }
// }

import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import {
  ChatHistorico,
  ConsultaHistoricoDetalle,
  MessageEntry,
} from '../../@models/message-entry';

@Injectable({
  providedIn: 'root',
})
export class ServiceComponent {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  sendMessage(message: MessageEntry): Observable<MessageEntry> {
    const body = {
      message: message.content,
      sessionId: message.id, // puedes usar crypto.randomUUID() desde el componente padre
    };

    return this.http
      .post<{ response: string }>(this.apiUrl + '/dialogflow', body)
      .pipe(
        map((res) => ({
          id: crypto.randomUUID(),
          content: res.response,
          role: 'assistant',
          createdAd: new Date(),
        }))
      );
  }

  //insertar historico de chat bot
  insertarChat(data: ChatHistorico): Observable<any> {
    return this.http.post<any>(this.apiUrl + '/insertarChatHistorico', data);
  }

  //consulta historico de chat bot
  getHistoricoPorUsuario(
    id_user: string
  ): Observable<ConsultaHistoricoDetalle[]> {
    const params = new HttpParams().set('id_user', id_user);
    return this.http.get<ConsultaHistoricoDetalle[]>(
      this.apiUrl + '/ConsultaHistoricoDetalle',
      { params }
    );
  }
}
