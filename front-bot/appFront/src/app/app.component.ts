// Toda libreria de imports en component va aqui
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
import {MatButtonModule} from '@angular/material/button';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatSidenavModule} from '@angular/material/sidenav';
import { ChatComponent } from './chat/chat.component';
import { LoginComponent } from './login/login.component';
import { BotComponent } from './bot/bot.component';




@Component({
  selector: 'app-root', 
  imports: [ MatToolbarModule, MatButtonModule, MatIconModule, MatSidenavModule, LoginComponent, BotComponent, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'PrivaBot';
  showFiller = false;
}
