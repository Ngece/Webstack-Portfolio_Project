from django import forms
from .models import Company, Ticket, Technician, Dispatcher

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'company_email', 'company_phone', 'company_address', 'company_city', 'company_state', 'company_zip',)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'completed', 'company',)


class TechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = ('technician_name', 'technician_email', 'technician_phone', 'technician_address', 'technician_city', 'technician_state', 'technician_zip', 'company',)


class DispatcherForm(forms.ModelForm):
    class Meta:
        model = Dispatcher
        fields = ('dispatcher_name', 'dispatcher_email', 'dispatcher_phone', 'dispatcher_address', 'dispatcher_city', 'dispatcher_state', 'dispatcher_zip', 'company',)