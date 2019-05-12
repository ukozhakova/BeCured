import { Component, OnInit } from '@angular/core';
import { IPatient, IDoctor } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';
import { Time } from '@angular/common';

@Component({
  selector: 'app-appointment',
  templateUrl: './appointment.component.html',
  styleUrls: ['./appointment.component.css']
})
export class AppointmentComponent implements OnInit {
  public name: any='';
  public text: any='';
  public patient: IPatient;
  public doctor: IDoctor;
  public date: Date;
  public time: Time;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }
  createAppointment(){
    if(this.name !== '' &&  this.text !== '' && this.patient.id !== 0 && this.doctor.id !== 0 ) {
    this.provider.createAppointment(this.name, this.text, this.patient, this.doctor,this.date, this.time).then( res => {
      console.log('appointment created');
      this.name = '';
      this.text = '';
      this.patient = null;
      this.doctor = null;
      })
    }
  }

}
