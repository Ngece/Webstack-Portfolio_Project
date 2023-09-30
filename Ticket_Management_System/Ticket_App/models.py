from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class SystemUser(AbstractUser):
    ROLE_CHOICES = (
        ('technician', 'Technician'),
        ('dispatcher', 'Dispatcher'),
        ('company', 'Company'),
    )
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='company')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True, blank=True)
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, null=True, blank=True, related_name='system_users')

    def __str__(self):
        return self.name + ' ' + self.role 


class Ticket(models.Model):
    ticket_choices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('accepted', 'Accepted'),
        ('monitored', 'Monitored'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed'),
    )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=ticket_choices, default='pending')
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(SystemUser, on_delete=models.CASCADE, null=True, blank=True, related_name='company_tickets')
    technician = models.ForeignKey(SystemUser, on_delete=models.CASCADE, null=True, blank=True, related_name='technician_tickets')
    dispatcher = models.ForeignKey(SystemUser, on_delete=models.CASCADE, null=True, blank=True, related_name='dispatcher_tickets')
    tech_comment = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title +  ' ' + self.status


class Feedback(models.Model):
    feedback_rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    feedback_status = (
        ('pending', 'Pending'),
        ('not_posted', 'Not Posted'),
        ('posted', 'Posted'),
    )
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=feedback_rating, default=1)
    status = models.CharField(max_length=100, choices=feedback_status, default='pending')