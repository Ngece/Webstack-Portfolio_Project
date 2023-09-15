from django.urls import path
from . import views
from .views import CompanyRegistrationView, TechnicianRegistrationView, DispatcherRegistrationView
from django.contrib.auth import views as auth_views


urlpatterns = [
        path('', views.home, name='home'),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('about/', views.about, name='about'),
        path('company_register/', views.CompanyRegistrationView.as_view(), name='company_register'),
        path('company_detail/', views.company_detail, name='company_detail'),
        path('company_update/', views.company_update, name='company_update'),
        path('user_tickets/', views.user_tickets, name='user_tickets'),
        path('create_ticket/', views.create_ticket, name='create_ticket'),
        path('ticket_detail/', views.ticket_detail, name='ticket_detail'),
        path('ticket_update/', views.ticket_update, name='ticket_update'),
        path('technician_create/', views.TechnicianRegistrationView.as_view(), name='technician_create'),
        path('technician_detail/', views.technician_detail, name='technician_detail'),
        path('technician_update/', views.technician_update, name='technician_update'),
        path('dispatcher_create/', views.DisptcherRegistrationView.as_view(), name='dispatcher_create'),
        path('dispatcher_detail/', views.dispatcher_detail, name='dispatcher_detail'),
        path('dispatcher_update/', views.dispatcher_update, name='dispatcher_update'),
]