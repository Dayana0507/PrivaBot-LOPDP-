import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { BotComponent } from './bot/bot.component';

// primera modificacion para la paginacion

export const routes: Routes = [
    { path: '', component: LoginComponent }, //raiz
  { path: 'bot', component: BotComponent } //a donde me quiero dirigir
];
