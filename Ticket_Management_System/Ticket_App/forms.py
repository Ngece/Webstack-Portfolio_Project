from .models import SystemUser, Company, Ticket, Feedback
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SystemUserForm(UserCreationForm):
    class Meta:
        model = SystemUser
        fields = ['name', 'surname', 'user_type']

class SystemUserUpdateForm(UserChangeForm):
    class Meta:
        model = SystemUser
        fields = ['name', 'surname', 'user_type']


class CompanyForm(UserCreationForm):
    class Meta:
        model = Company
        fields = ['name', 'contact', 'address', 'city', 'surbub', 'zip_code']

class CompanyUpdateForm(UserChangeForm):
    class Meta:
        model = Company
        fields = ['name', 'contact', 'address', 'city', 'surbub', 'zip_code']


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'company']

class TicketUpdateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'status', 'company', 'technician', 'dispatcher']

        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'name', 'comment', 'rating']

