import {BrowserModule} from '@angular/platform-browser';
import {ClassProvider, NgModule} from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import {AppComponent} from './app.component';
import {ProviderService} from './shared/services/provider.service';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';
import {FormsModule} from '@angular/forms';
import {AuthInterceptor} from './AuthInterceptor';
import { AppRoutingModule } from './app-routing.module';
import { MainComponent } from './main/main.component';
import { FooterComponent } from './footer/footer.component';
import { HeaderComponent } from './header/header.component';
import { LoginComponent } from './login/login.component';
import { DoctorComponent } from './doctor/doctor.component';
import { TreatmentComponent } from './treatment/treatment.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    FooterComponent,
    HeaderComponent,
    LoginComponent,
    DoctorComponent,
    TreatmentComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
