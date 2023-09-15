from django.contrib.auth.models import AbstractUser
from django.db import models

class Company(AbstractUser):
    company_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.company_name} {self.contact}"


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket_title = models.CharField(max_length=50)
    ticket_description = models.CharField(max_length=100)
    ticket_status = models.CharField(max_length=50)
    ticket_priority = models.CharField(max_length=50)
    ticket_service = models.CharField(max_length=50)
    ticket_company = models.ForeignKey('Company', on_delete=models.CASCADE)
    ticket_technician = models.ForeignKey('Technician', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ticket_title} {self.ticket_status} {self.ticket_company} {self.created_at}"


class Technician(AbstractUser):
    technician_name = models.CharField(max_length=50)
    technician_surname = models.CharField(max_length=50)
    technician_email = models.EmailField() 
    technician_phone = models.CharField(max_length=15)
    technician_company = models.ForeignKey('Company', on_delete=models.CASCADE)
    technician_ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.technician_name} {self.technician_email} {self.technician_phone} {self.technician_company}"


class Dispatcher(AbstractUser):
    dispatcher_name = models.CharField(max_length=50)
    dispatcher_surname = models.CharField(max_length=50)
    dispatcher_email = models.EmailField()
    dispatcher_phone = models.CharField(max_length=15)
    dispatcher_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.dispatcher_name} {self.dispatcher_email} {self.dispatcher_phone} {self.dispatcher_company}"
