import { Component } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { ChatComponent } from '../chat/chat.component';
import { ServiceComponent } from '../services/service/service.component';
import { ChangeDetectionStrategy, inject, signal } from '@angular/core';
import { ConsultaHistoricoDetalle } from '../@models/message-entry';
import { CommonModule } from '@angular/common';



@Component({
  selector: 'app-bot',
  imports: [
    CommonModule,
    MatToolbarModule,
    MatButtonModule,
    MatIconModule,
    MatSidenavModule,
    ChatComponent,
  ],
  standalone: true,
  templateUrl: './bot.component.html',
  styleUrls: ['./bot.component.css'],
})
export class BotComponent {
  title = 'PrivaBot';
  showFiller = false;
  private readonly service = inject(ServiceComponent);
  historico: ConsultaHistoricoDetalle[] = [];
  userData: { id: number; email: string } = { id: 0, email: '' };
  historiales: any[][] = []; // Historiales separados
  historialSeleccionado: any[] | null = null; // Historial activo que se mostrará
  ngOnInit() {
    const stored = localStorage.getItem('userData');

    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        if (parsed && parsed.id && parsed.email) {
          this.userData = parsed;
          console.log('👤 Datos usuario desde localStorage:', this.userData);
          this.cargarHistorico(this.userData.id.toString());
        } else {
          console.warn(
            '⚠️ userData en localStorage no tiene formato esperado:',
            parsed
          );
        }
      } catch (e) {
        console.error('❌ Error al parsear userData:', e);
      }
    } else {
      console.warn('⚠️ No se encontró userData en localStorage');
    }
  }

  cargarHistorico(id: string) {
    this.service.getHistoricoPorUsuario(id).subscribe({
      next: (data) => {
        try {
          // Parsear cada historial por separado
          this.historiales = data.map((item) => JSON.parse(item.historial));
          this.historialSeleccionado = null; // Limpia la selección previa
          console.log('historial', this.historiales);
        } catch (e) {
          console.error('Error al parsear historiales:', e);
          this.historiales = [];
        }
      },
      error: (error) => {
        console.error('Error al cargar histórico:', error);
      },
    });
  }

  mostrarHistorialCompleto(index: number) {
    // this.historialSeleccionado = this.historiales[index];
     if (this.historialSeleccionado === this.historiales[index]) {
      this.historialSeleccionado = null; // Si ya está visible, lo oculta
    } else {
      this.historialSeleccionado = this.historiales[index]; // Si no, lo muestra
    }

  }



  agregarAlHistorial(nuevoHistorial: any) {
  // Lo inserta al inicio del array para que sea el #1
  this.historiales.unshift(nuevoHistorial);
  console.log('🆕 Historial agregado:', nuevoHistorial);
  
}



  
}




