import { Component, OnInit } from '@angular/core';
import { IDoctor, IPatient, IAppointment, ITreatment, IAuthResponse } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public doctors: IDoctor[] = [];
  public patients: IPatient[] = [];
  public appointments: IAppointment[] = [];
  public treatments: ITreatment[] = [];

  public loading = false;
  public isLogged = false;

  public name: any='';
  public surname: any='';
  public speciality: any='';
  public patient_diagnosis: any='';
  public gender: any='';
  public phone_number: any='';
  public email_address: any='';

  public pname: any='';
  public psurname: any='';
  public age: any='';
  public diagnosis: any='';
  public pgender: any='';
  public mobile: any = '';
  public address: any = '';
  public allergies: any='';

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

  getPatients(){
    this.provider.getPatients().then(res =>{
      this.patients = res;
    }); 
  }
  
  getAppointments(){
    this.provider.getAppointments().then(res =>{
      this.appointments = res;
    }); 
  }
  
  getTreatments(){
    this.provider.getTreatments().then(res =>{
      this.treatments = res;
    }); 
  }

  updateDoctor(c: IDoctor){
    this.provider.updateDoctor(c).then(res =>{
      console.log(c.name+' updated');
    });
  }

  createDoctor(){
    if(this.name !== '' &&  this.surname !== '' &&
    this.speciality !== '' &&  this.patient_diagnosis !== ''&& 
    this.gender !== '' &&  this.phone_number !== '' && this.email_address !== '') {
    this.provider.createDoctor(this.name, this.surname, this.speciality, this.patient_diagnosis,
      this.gender, this.phone_number, this.email_address).then( res => {
      this.name = '';
      this.surname = '';
      this.speciality = '';
      this.patient_diagnosis = '';
      this.gender = '';
      this.phone_number = '';
      this.email_address = '';
      this.doctors.push(res);
      })
    }
  }


  deleteDoctor(c: IDoctor){
    this.provider.deleteDoctor(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getDoctors().then( res => {
        this.doctors = res;
      })
    })
  }

  deletePatient(c: IPatient){
    this.provider.deletePatient(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getPatients().then( res => {
        this.patients = res;
      })
    })
  }

  deleteAppointment(c: IAppointment){
    this.provider.deleteAppointment(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getAppointments().then( res => {
        this.appointments = res;
      })
    })
  }

  deleteTreatment(c: ITreatment){
    this.provider.deleteTreatment(c.id).then(res => {
      console.log(c.name + ' deleted');
      this.provider.getTreatments().then( res => {
        this.treatments = res;
      })
    })
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


  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
    });
  }
}