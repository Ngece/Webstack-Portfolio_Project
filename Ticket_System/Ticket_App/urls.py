from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Ticket_list/', views.Ticket_list, name='Ticket_list'),
    path('Ticket_registration/', views.Ticket_registration, name='Ticket_registration'),
    path('Company_list/', views.Company_list, name='Company_list'),
    path('Company_registration/', views.Company_registration, name='Company_registration'),
    path('Technician_list/', views.Technician_list, name='Technician_list'),
    path('Technician_registration/', views.Technician_registration, name='Technician_registration'),
    path('Dispatcher_list/', views.Dispatcher_list, name='Dispatcher_list'),
    path('Dispatcher_registration/', views.Dispatcher_registration, name='Dispatcher_registration'),
]