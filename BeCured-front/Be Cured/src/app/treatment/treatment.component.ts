import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IPatient, IDoctor } from '../shared/models/models';

@Component({
  selector: 'app-treatment',
  templateUrl: './treatment.component.html',
  styleUrls: ['./treatment.component.css']
})
export class TreatmentComponent implements OnInit {
  public name: any='';
  public description: any='';
  public patient: IPatient;
  public doctor: IDoctor;

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    
  }

  createTreatment(){
    if(this.name !== '' &&  this.description !== '' && this.patient.id !== 0 && this.doctor.id !== 0 ) {
    this.provider.createTreatment(this.name, this.description, this.patient, this.doctor).then( res => {
      console.log('treatment created');
      this.name = '';
      this.description = '';
      this.patient = null;
      this.doctor = null;
      })
    }
  }

}
