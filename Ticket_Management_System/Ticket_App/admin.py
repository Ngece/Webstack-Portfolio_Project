from django.contrib import admin
from .models import Ticket, Feedback

# Registering the models on admin
admin.site.register(Ticket)
admin.site.register(Feedback)
