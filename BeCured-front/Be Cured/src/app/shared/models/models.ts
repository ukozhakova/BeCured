export interface IDoctor{
    id: number;
    name: string;
    surname: string;
    address: string;
    mobile: string;
    dob: Date;
    speciality: string;
    gender: string;
    qualification: string;
  }
  
export interface IPatient{
    id: number;
    name: string;
    surname: string;
    diagnosis: string;
    age: number;
    gender: string;
    mobile: string;
    email_address: string;
    address: string;
    allergies: string;
    doctor: IDoctor;
  }

export interface IReceptionist{
    id: number;
    name: string;
    surname: string;
    mobile: string;
    dob: Date;
    gender: string;
  }

export interface ITreatment{
    patient: IPatient;
    doctor: IDoctor;
    title: string;
    description: string;
    created_at: Date;
    updated_at: Date;
  }
  export interface IAppointment{
    patient: IPatient;
    doctor: IDoctor;
    time: Date;
  }
  export interface IBill{
    date: Date;
    patient: IPatient;
    doctor: IDoctor;
    treatment: ITreatment;
    amount: number;
  }