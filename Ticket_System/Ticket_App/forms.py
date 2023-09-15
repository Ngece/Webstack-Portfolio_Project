from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Technician, Dispatcher, Ticket

class CompanyRegistrationForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ('username', 'email', 'password1', 'password2', 'company_name', 'contact', 'address', 'city', 'state', 'zipcode')



class TechnicianRegistrationForm(UserCreationForm):
    class Meta:
        model = Technician
        fields = ('username', 'email', 'password1', 'password2', 'technician_name', 'technician_surname', 'technician_phone', 'technician_company', 'technician_ticket')


class DispatcherRegistrationForm(UserCreationForm):
    class Meta:
        model = Dispatcher
        fields = ('username', 'email', 'password1', 'password2', 'dispatcher_name', 'dispatcher_surname', 'dispatcher_phone', 'dispatcher_company')


class TicketCreationForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_title', 'ticket_description', 'ticket_status', 'ticket_priority', 'ticket_service', 'ticket_company', 'ticket_technician']
