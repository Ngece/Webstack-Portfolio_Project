from django.contrib import admin
from .models import Company, Ticket, Technician, Dispatcher

# Register your models here.
admin.site.register(Company)
admin.site.register(Ticket)
admin.site.register(Technician)
admin.site.register(Dispatcher)
