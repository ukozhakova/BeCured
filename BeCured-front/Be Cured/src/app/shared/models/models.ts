export interface IDoctor{
    id: number;
    name: string;
    surname: string;
    speciality: string;
    phone_number: string; 
    email_address: string;
  }
  
export interface IPatient{
    id: number;
    name: string;
    surname: string;
    diagnosis: string;
    age: number;
    gender: string;
    phone_number: string;
    email_address: string;
    allergies: string;
  }

export interface IRequest{
    id: number;
    name: string;
    text: string;
    created_at: Date;
  }

export interface IResponse{
    id: number;
    name: string;
    text: string;
    created_at: Date;
  }