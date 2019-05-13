import { Component, OnInit } from '@angular/core';
import { ITreatment,IDoctor, IAppointment } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrls: ['./patient.component.css']
})
export class PatientComponent implements OnInit {
  public treatments: ITreatment[] = [];
  public doctors: IDoctor[] = [];
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
      this.getTreatments();
      this.getDoctors();
    }

  }

  getTreatments(){
    this.provider.getTreatments().then(res =>{
      this.treatments=res;
      setTimeout( ()=>{
        this.loading=true;
      },100);
    });
  }
  
  getDoctors(){
    this.provider.getDoctors().then(res =>{
      this.doctors = res;
      setTimeout( () => {
        this.loading=true;
      }, 100);
    }); 
  }


  auth(){
    if (this.login !== '' && this.login[0] == 'p' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        this.isLogged = true;
        this.getTreatments();
        this.getDoctors();
      });
    }
  }

}
