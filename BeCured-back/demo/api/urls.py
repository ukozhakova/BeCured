from django.urls import path, re_path
from django.conf.urls import url
from .auth import logout, login
from . import views

urlpatterns = [
    path('doctor_lists/', views.DoctorList.as_view()),
    path('doctor_lists/<int:pk>/', views.DoctorDetail.as_view()),

    path('treatment_lists/', views.TreatmentLists),
    path('treatment_lists/<int:pk>/', views.TreatmentListsDetail),

    path('patient_lists/', views.PatientList.as_view()),
    path('patient_lists/<int:pk>/', views.PatientDetail.as_view()),

    path('appointment_lists/', views.AppointmentLists.as_view()),
    path('appointment_lists/<int:pk>/', views.AppointmentListDetail.as_view()),

    path('login/', login),
    path('logout/', logout),
   # path('users/', views.PersonList.as_view()),

    path('home/', views.home)
    #path('create_user/', views.create_user_profile)
]
