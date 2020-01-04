from django.contrib import admin
# imported the Job model from models of the app by me
from .models import Job
# passed the Job model to the admin by me
admin.site.register(Job)