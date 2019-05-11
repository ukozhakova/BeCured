import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IDoctor, IPatient, IAppointment, ITreatment, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService{
  constructor(http: HttpClient) {
    super(http);
 }
  getDoctors(): Promise<IDoctor[]>{
    return this.get('http://127.0.0.1:8000/api/doctor_lists/', {});
  }

  getPatients(): Promise<IPatient[]>{
    return this.get('http://127.0.0.1:8000/api/patient_lists/', {});
  }

  getAppointments(): Promise<IAppointment[]>{
    return this.get('http://127.0.0.1:8000/api/appointment_lists/', {});
  }

  getTreatments(): Promise<ITreatment[]>{
    return this.get('http://127.0.0.1:8000/api/treatment_lists/', {});
  }

  deleteDoctor(id: number) : Promise<IDoctor[]>{
    return this.delete(`http://localhost:8000/api/doctor_lists/${id}`,{});
  }

  deletePatient(id: number) : Promise<IPatient[]>{
    return this.delete(`http://localhost:8000/api/patient_lists/${id}`,{});
  }

  deleteAppointment(id: number) : Promise<IAppointment[]>{
    return this.delete(`http://localhost:8000/api/appointment_lists/${id}`,{});
  }

  deleteTreatment(id: number) : Promise<ITreatment[]>{
    return this.delete(`http://localhost:8000/api/treatment_lists/${id}`,{});
  }

  updateDoctor(doctors: IDoctor): Promise<IDoctor>{
    return this.put(`http://localhost:8000/api/doctor_lists/${doctors.id}/`,{
      name: doctors.name,
      surname: doctors.surname,
      speciality: doctors.speciality,
      patient_diagnosis: doctors.patient_diagnosis,
      gender: doctors.gender,
      phone_number: doctors.phone_number,
      email_address: doctors.email_address
    });
  }


  createDoctor(name: any, surname: any, speciality: any, patient_diagnosis: any, gender: any, phone_number: any, email_address: any) : Promise<IDoctor>{
    return this.post(`http://localhost:8000/api/doctor_lists/`, {
      name: name,
      surname: surname,
      speciality: speciality,
      patient_diagnosis: patient_diagnosis,
      gender: gender,
      phone_number: phone_number,
      email_address: email_address,
    });
  }
  
  auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }
}
