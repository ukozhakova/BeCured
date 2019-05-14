import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { MainComponent } from './main/main.component';
import { DoctorComponent } from './doctor/doctor.component';
import { TreatmentComponent } from './treatment/treatment.component';
import { PatientComponent } from './patient/patient.component';
import { AppointmentComponent } from './appointment/appointment.component';


const routes: Routes = [
  { path: '', component: LoginComponent },
  { path: 'main', component: MainComponent },
  { path: 'doctor', component: DoctorComponent },
  { path: 'treatment', component: TreatmentComponent },
  { path: 'patient', component: PatientComponent},
  { path: 'appointment', component: AppointmentComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
