import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IDoctor, IPatient, IAppointment, ITreatment, IAuthResponse } from '../models/models';
import { Time } from '@angular/common';
import { all } from 'q';

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

  updatePatient(patient: IPatient) : Promise<IPatient>{
    return this.put(`http://localhost:8000/api/patient_lists/${patient.id}/`,{
      name: patient.name,
      surname: patient.surname,
      age: patient.age,
      diagnosis: patient.diagnosis,
      gender: patient.gender,
      mobile: patient.mobile,
      address: patient.address,
      allergies: patient.allergies,
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

  createPatient(name: any, surname: any, age: any, diagnosis: any, gender: any, mobile: any, address: any, allergies: any) : Promise<IPatient>{
    return this.post(`http://localhost:8000/api/patient_lists/`, {
      name: name,
      surname: surname,
      age: age,
      diagnosis: diagnosis,
      gender: gender,
      mobile: mobile,
      address: address,
      allergies: allergies,
    });
  }

  createTreatment(name: any, description: any, patient: IPatient, doctor: IDoctor) : Promise<ITreatment>{
    return this.post(`http://localhost:8000/api/treatment_lists/`, {
      name: name,
      description: description,
      patient: patient,
      doctor: doctor,
    });
  }

  createAppointment(name: any, text: any, patient: IPatient, doctor: IDoctor, date: Date, time: Time) : Promise<IAppointment>{
    return this.post(`http://localhost:8000/api/appointment_lists/`,{
      name: name,
      text: text,
      patient: patient,
      doctor: doctor,
      date: date,
      time: time
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
