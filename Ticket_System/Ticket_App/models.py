from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=100, default='No Name Provided')
    company_email = models.EmailField(max_length=100, default='No Email Provided')
    company_phone = models.CharField(max_length=13, default='No Email Provided')
    company_address = models.CharField(max_length=100, default='No Address Provided')
    company_city = models.CharField(max_length=100, default='No City Provided')
    company_state = models.CharField(max_length=100, default='No State Provided')
    company_zip = models.CharField(max_length=5, default='No ZipCode Provided')

    def __str__(self):
        return self.company_name


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title 


class Technician(models.Model):
    technician_name = models.CharField(max_length=100)
    technician_email = models.EmailField(max_length=100)
    technician_phone = models.CharField(max_length=13)
    technician_address = models.CharField(max_length=100)
    technician_city = models.CharField(max_length=100)
    technician_state = models.CharField(max_length=100)
    technician_zip = models.CharField(max_length=5)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.technician_name


class Dispatcher(models.Model):
    dispatcher_name = models.CharField(max_length=100)
    dispatcher_email = models.EmailField(max_length=100)
    dispatcher_phone = models.CharField(max_length=13)
    dispatcher_address = models.CharField(max_length=100)
    dispatcher_city = models.CharField(max_length=100)
    dispatcher_state = models.CharField(max_length=100)
    dispatcher_zip = models.CharField(max_length=5)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.dispatcher_name