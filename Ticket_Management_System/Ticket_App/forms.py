from .models import Ticket, Feedback
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['name', 'phone']


class SystemUserUpdateForm(UserChangeForm):
    class Meta:
        model = SystemUser
        fields = ['name', 'phone']


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
