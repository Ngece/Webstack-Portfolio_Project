from .models import Ticket, Feedback, SystemUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserSignUpForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=SystemUser.ROLE_CHOICES,  # Use the choices from your SystemUser model
        required=False,  # Make the field not required
    )
    
    class Meta:
        model = SystemUser
        fields = ['role', 'name', 'phone', 'email', 'username']

class SystemUserUpdateForm(UserChangeForm):
    class Meta:
        model = SystemUser
        fields = ['role','name', 'phone', 'email', 'username']


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