from django.contrib import admin
from .models import SystemUser, Company, Ticket, Feedback

# Registering the models on admin
admin.site.register(SystemUser)
admin.site.register(Company)
admin.site.register(Ticket)
admin.site.register(Feedback)
