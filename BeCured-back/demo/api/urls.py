from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.main),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('doctor_lists/', views.doctorLists.as_view()),
    path('doctor_lists/<int:pk>/', views.doctorListDetail),
    path('patient_page', views.patientPage),
    path('response_lists/', views.responseLists.as_view()),
    path('response_lists/<int:pk>/', views.responseListDetail),
    path('request_page', views.requestPage),
    path('doctor_page', views.doctorPage),
    path('patient_lists/', views.patientLists.as_view()),
    path('patient_lists/<int:pk>/', views.patientListDetail),
    path('add_patient', views.addPatient),
    path('request_lists/', views.requestLists.as_view()),
    path('request_lists/<int:pk>/', views.requestListDetail),
    path('response_page', views. responsePage),

    path('login/', views.login),
    path('logout/', views.logout),
    # path('users/', views.UserList.as_view()),
]
