import { Time } from '@angular/common';

export interface IDoctor{
    id: number;
    name: string;
    surname: string;
    speciality: string;
    patient_diagnosis: string;
    gender: string;
    email_address: string;
    phone_number: string;
  }

export interface IPatient{
    id: number;
    name: string;
    surname: string;
    age: number;
    diagnosis: string;
    gender: string;
    mobile: string;
    address: string;
    allergies: string;
  }

export interface IAppointment{
    id: number;
    name: string;
    text: string;
    created_at: Date;
    time: Time;
  }

export interface ITreatment{
    id: number;
    name: string;
    description: string;
    created_at: Date;
    updated_at: Date;
}  
 
export interface IAuthResponse{
    token: string;
  }