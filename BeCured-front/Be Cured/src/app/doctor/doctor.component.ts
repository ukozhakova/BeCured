import { Component, OnInit } from '@angular/core';
import { IAppointment } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-doctor',
  templateUrl: './doctor.component.html',
  styleUrls: ['./doctor.component.css']
})
export class DoctorComponent implements OnInit {
  public appointments: IAppointment[] = [];

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
      this.getAppointments();
    }

  }
  
  getAppointments(){
    this.provider.getAppointments().then(res =>{
      this.appointments = res;
      setTimeout( () => {
        this.loading=true;
      }, 100);
    }); 
  }


  auth(){
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getAppointments();
      });
    }
  }

}
