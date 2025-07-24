import { ChangeDetectionStrategy, Component, inject, signal, OnInit, OnDestroy } from '@angular/core';
import { ChatInputComponent } from '../chat-input/chat-input.component';
import { MessageListComponent } from '../message-list/message-list.component';
import { ChatHistorico, MessageEntry } from '../@models/message-entry';
import { ServiceComponent } from '../services/service/service.component';

@Component({
  selector: 'app-chat',
  standalone: true,
  imports: [ChatInputComponent, MessageListComponent],
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ChatComponent implements OnInit, OnDestroy {
  messageEntries = signal<MessageEntry[]>([]);
  private readonly service = inject(ServiceComponent);
  chatLog: { mensaje: string; respuesta: string }[] = [];
  email = '';
  userData: { id: number; email: string } = { id: 0, email: '' };
  private timeout: any;  // Temporizador de inactividad
  private timeoutDuration: number = 60000;  // 1 minuto
  private inactivityTimeout: any; // El temporizador de inactividad que se reiniciará

  ngOnInit() {
    const stored = localStorage.getItem('userData');

    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        if (parsed && parsed.id && parsed.email) {
          this.userData = parsed;
          console.log('👤 Datos usuario desde localStorage:', this.userData);
        } else {
          console.warn('⚠️ userData en localStorage no tiene formato esperado:', parsed);
        }
      } catch (e) {
        console.error('❌ Error al parsear userData:', e);
      }
    } else {
      console.warn('⚠️ No se encontró userData en localStorage');
    }

    // Iniciar temporizador de inactividad
    this.resetInactivityTimer();
  }

  ngOnDestroy() {
    if (this.inactivityTimeout) {
      clearTimeout(this.inactivityTimeout); // Limpiar el temporizador al destruir el componente
    }
  }

  // Función para guardar automáticamente después de un minuto de inactividad
  private saveChatAutomatically() {
    console.log('🕒 Guardando chat automáticamente...');
    
    // Solo guardar si el chatLog tiene mensajes
    if (this.chatLog.length > 0 && this.chatLog.some(entry => entry.mensaje.trim() !== "" && entry.respuesta.trim() !== "")) {
      this.enviarChat(); // Llama a la función de enviar chat solo si hay mensajes
    } else {
      console.log('❌ No se guardó el chat porque está vacío.');
    }
    this.messageEntries.set([]); // Limpia mensajes en pantalla

  }

  // Reinicia el temporizador de inactividad
  private resetInactivityTimer() {
    if (this.inactivityTimeout) {
      clearTimeout(this.inactivityTimeout); // Limpiar cualquier temporizador anterior
    }

    // Establecer el nuevo temporizador que se ejecutará después de 1 minuto de inactividad
    this.inactivityTimeout = setTimeout(() => {
      this.saveChatAutomatically();
    }, this.timeoutDuration);
  }

  // Esta función es llamada cuando el usuario envía un mensaje
  public updateMessageEntries(message: MessageEntry): void {
    this.messageEntries.update((prev) => [...prev, message]);

    this.service.sendMessage(message).subscribe((response) => {
      this.messageEntries.update((prev) => [...prev, response]);

      this.chatLog.push({
        mensaje: message.content,
        respuesta: response.content,
      });

      console.debug('📦 Chat log actualizado:', this.chatLog);
      console.debug('📦 Chat log actualizado:', response);

      // Reinicia el temporizador cada vez que el usuario envíe un mensaje
      this.resetInactivityTimer();
    });
  }

  // Función para enviar el chat a la base de datos
  enviarChat() {
    const payload: ChatHistorico = {
      id_user: this.userData.id,
      email: this.userData.email,
      chatLog: this.chatLog,
    };

    this.service.insertarChat(payload).subscribe({
      next: (res) => {
        console.log('✅ Respuesta del servidor:', res);
      },
      error: (err) => {
        console.error('❌ Error al enviar:', err);
      },
    });
  }

  
}
