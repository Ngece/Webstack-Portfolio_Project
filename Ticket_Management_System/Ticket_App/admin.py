from django.contrib import admin
from .models import Ticket, Feedback, SystemUser

# Registering the models on admin
admin.site.register(SystemUser)
admin.site.register(Ticket)
admin.site.register(Feedback)
