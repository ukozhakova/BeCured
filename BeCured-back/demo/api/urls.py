from django.urls import path, re_path
from . import views
urlpatterns = [
    # path('', views.main),
    path('signin/', views.signin),
    # path('signup/', views.signup),
    path('doctor_lists/', views.DoctorList.as_view()),
    path('doctor_lists/<int:pk>/', views.DoctorDetail.as_view()),
    path('patient_lists/', views.PatientList.as_view()),
    path('patient_lists/<int:pk>/', views.PatientDetail.as_view()),
    path('receptionist_detail/', views.ReceptionistDetail.as_view()),
    path('bill/', views.BillDetail.as_view()),
    path('logout/', views.logout),
    path('users/', views.UserList.as_view()),
]
