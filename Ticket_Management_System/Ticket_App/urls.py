from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
     
    path('Ticket_registration/', views.Ticket_registration, name='Ticket_registration'),
    path('Ticket_detail/<int:pk>/', views.Ticket_detail, name='Ticket_detail'),
    path('Update_ticket/<int:pk>/', views.Update_ticket, name='Update_ticket'),
    path('All_ticket_list/', views.All_ticket_list, name='All_ticket_list'),
    path('Approved_ticket_list/', views.Approved_ticket_list, name='Approved_ticket_list'),
    path('My_ticket_list/', views.My_ticket_list, name='My_ticket_list'),
    path('Approve_ticket/<int:pk>/', views.Approve_ticket, name='Approve_ticket'),
    path('Accept_ticket/<int:pk>/', views.Accept_ticket, name='Accept_ticket'),
    path('Reject_ticket/<int:pk>/', views.Reject_ticket, name='Reject_ticket'),
    path('Close_ticket/<int:pk>/', views.Close_ticket, name='Close_ticket'),
    path('Delete_ticket/<int:pk>/', views.Delete_ticket, name='Delete_ticket'),

    path('Company_registration/', views.Company_registration, name='Company_registration'),
    path('Company_detail/<int:pk>/', views.Company_detail, name='Company_detail'),
    path('All_company_list/', views.All_company_list, name='All_company_list'),

    path('Technician_registration/', views.Technician_registration, name='Technician_registration'),
    path('Technician_detail/<int:pk>/', views.Technician_detail, name='Technician_detail'),
    path('All_technician_list/', views.All_technician_list, name='All_technician_list'),

    path('Dispatcher_registration/', views.Dispatcher_registration, name='Dispatcher_registration'),
    path('Dispatcher_detail/<int:pk>/', views.Dispatcher_detail, name='Dispatcher_detail'),
    path('All_dispatcher_list/', views.All_dispatcher_list, name='All_dispatcher_list'),

    path('Update_profile/', views.Update_user_profile, name='Update_profile'),

    path('Feedback_registration/', views.Feedback_registration, name='Feedback_registration'),
    path('Feedback_detail/<int:pk>/', views.Feedback_detail, name='Feedback_detail'),
    path('Feedback_list/', views.Feedback_list, name='Feedback_list'),
    path('Post_feedback/<int:pk>/', views.Post_feedback, name='Post_feedback'),
    path('Remove_feedback/<int:pk>/', views.Remove_feedback, name='Remove_feedback'),
    path('Delete_feedback/<int:pk>/', views.Delete_feedback, name='Delete_feedback')
]