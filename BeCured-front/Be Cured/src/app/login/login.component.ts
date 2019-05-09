import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IDoctor } from '../shared/models/models';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public doctors: IDoctor[] = [];
  public loading = false;
  public isLogged = false;

  public login: any='';
  public password: any='';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    const token = localStorage.getItem('token');
    if (token) {
      this.isLogged = true;
    }

    if(this.isLogged){
      this.getDoctors();
    }

  }

  getDoctors(){
    this.provider.getDoctors().then(res =>{
      this.doctors = res;
      setTimeout( () => {
        this.loading=true;
      }, 1000);
    }); 
  }


  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getDoctors();
      });
    }
  }
}
