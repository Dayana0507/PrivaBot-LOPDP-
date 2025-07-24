import { Component, input } from '@angular/core';
import { MessageEntry } from '../../@models/message-entry';
import {MatIconModule} from '@angular/material/icon';


@Component({
  selector: 'app-user-message-entry',
  imports: [MatIconModule],
  templateUrl: './user-message-entry.component.html',
  styleUrls: ['./user-message-entry.component.css']
})
export class UserMessageEntryComponent {
  messageEntry = input<MessageEntry>();
}
