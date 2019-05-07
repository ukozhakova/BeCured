from django.urls import path, re_path
from . import views
urlpatterns = [
    path('login/', views.login),
    path('doctor_lists/', views.DoctorList.as_view()),
    path('doctor_lists/<int:pk>/', views.DoctorDetail.as_view()),
    path('patient_lists/', views.PatientList.as_view()),
    path('patient_lists/<int:pk>/', views.PatientDetail.as_view()),
    path('receptionist_lists/<int:pk>/', views.ReceptionistDetail.as_view()),
    path('treatment_lists/<int:pk>/', views.TreatmentDetail.as_view()),
    path('appointment_lists/<int:pk>/', views.AppointmentDetail.as_view()),
    path('bill_lists/<int:pk>/', views.BillDetail.as_view()),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
]
