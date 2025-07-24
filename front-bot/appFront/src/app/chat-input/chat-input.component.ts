import {
  ChangeDetectionStrategy,
  Component,
  ElementRef,
  output,
  ViewChild,
} from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MessageEntry } from '../@models/message-entry';
import { v4 as uuidv4 } from 'uuid';

@Component({
  selector: 'app-chat-input',
  imports: [MatIconModule, MatButtonModule],
  templateUrl: './chat-input.component.html',
  styleUrls: ['./chat-input.component.css'],
  changeDetection: ChangeDetectionStrategy.OnPush,
})
export class ChatInputComponent {
  // vista secundaria
  @ViewChild('messageInput') messageInput!: ElementRef<HTMLDivElement>;

  public message = output<MessageEntry>();

  public sendMessage(): void {
    const message = this.messageInput.nativeElement.innerText;
    console.debug('Entrada usuario--->', message);
    this.message.emit({
      id: crypto.randomUUID(),
      content: message,
      role: 'user',
      createdAd: new Date(),
    });
    this.messageInput.nativeElement.innerText='' //para limpiar la caja de texto
  }

  // this.messageInput.nativeElement.innerText

  // public message = output<MessageEntry>();
  // sendMessage(): void {
  //   const message = this.messageInput?.nativeElement.textContent?.trim();
  //   if (message) {
  //     console.log('Sending message:', message);
  //     const messageEntry: MessageEntry = {
  //       id: crypto.randomUUID(),
  //       content: message,
  //       role: 'user',
  //       createdAt: new Date(),
  //     };
  //     this.message.emit(messageEntry);
  //     if (this.messageInput) {
  //       this.messageInput.nativeElement.textContent = '';
  //     }
  //   } else {
  //     console.log('Message is empty, not sending.');
  //   }
  // }
}
