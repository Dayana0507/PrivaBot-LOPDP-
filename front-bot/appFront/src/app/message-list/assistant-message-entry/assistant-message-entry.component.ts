import { Component, input, signal, WritableSignal } from '@angular/core';
import { MessageEntry } from '../../@models/message-entry';
import {MatIconModule} from '@angular/material/icon';


@Component({
  selector: 'app-assistant-message-entry',
  imports: [MatIconModule],
  templateUrl: './assistant-message-entry.component.html',
  styleUrl: './assistant-message-entry.component.css'
})
export class AssistantMessageEntryComponent {
  messageEntry = input<MessageEntry>();

  //Agregar simulacion de pensamiento
  // public isThinking: WritableSignal<boolean> = signal(true);

  // public ngOnInit():void{
  //   this.isThinking.set(true);
  // }
}
