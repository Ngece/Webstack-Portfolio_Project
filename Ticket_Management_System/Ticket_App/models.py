from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth.models import Group, Permission


# Create your models here.
class SystemUser(AbstractUser):
    user_choices = (
        ('dispatcher', 'Dispatcher'),
        ('technician', 'Technician')
    )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=user_choices, default='dispatcher')
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, null=True, blank=True, related_name='system_users')

    def __str__(self):
        return self.name + ' ' + self.user_type


class Company(AbstractUser):
    is_company = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=13)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    surbub = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='company_groups',
        related_query_name='company_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='company_user_permissions',
        related_query_name='company_user_permission',
    )

    def __str__(self):
        return self.name


class Ticket(models.Model):
    ticket_choices = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('closed', 'Closed')
    )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=ticket_choices, default='pending')
    description = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    technician = models.ForeignKey(SystemUser, on_delete=models.CASCADE, null=True, blank=True, related_name='technician_tickets')
    dispatcher = models.ForeignKey(SystemUser, on_delete=models.CASCADE, null=True, blank=True, related_name='dispatcher_tickets')

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