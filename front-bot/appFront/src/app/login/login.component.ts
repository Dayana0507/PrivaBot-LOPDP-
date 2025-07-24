import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';


//segunda modificacion para la paginacion
@Component({
  selector: 'app-login',  
  standalone: true,
  imports: [FormsModule,HttpClientModule,  RouterModule], //esta sirve para el formulario
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {
  email: string = '';
  // constructor(private http: HttpClient,private router: Router) {} //paginacion

  constructor(private http: HttpClient, private router: Router) {}

onLogin() {
  const payload = { email: this.email };

  this.http.post('http://localhost:5000/login', payload, { observe: 'response' })
    .subscribe({
      next: (res) => {
        console.log('Respuesta completa:', res);

        if (res.status === 200) {
          localStorage.removeItem('userData');
          localStorage.setItem('userData', JSON.stringify(res.body));

          this.router.navigate(['/bot']);
        } else {
          console.warn('Login fallido con estado:', res.status);
        }
      },
      error: (err) => {
        console.error('Error en el login:', err);
      }
    });

}



  //  onLogin() {
  // const payload = { email: this.email };
  // this.http.post('http://localhost:5000/login', payload, { observe: 'response' })
  //   .subscribe({
  //     next: (res) => {
  //       console.log('Respuesta completa:', res);

  //       if (res.status === 200) {
  //          this.router.navigate(['/bot'], { state: { user: res.body } });

  //       } else {
  //         console.warn('Login fallido con estado:', res.status);
  //         // Puedes mostrar un mensaje en pantalla si deseas
  //       }
  //     },
  //     error: (err) => {
  //       console.error('Error en el login:', err);
  //       // Aquí también puedes mostrar un mensaje al usuario
  //     }
  //   });
// }
}
