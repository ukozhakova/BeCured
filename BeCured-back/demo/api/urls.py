from django.urls import path
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

    path('login/', views.login),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
]
