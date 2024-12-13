from django.contrib import admin
from .models import User, Plan, Task, Report

admin.site.register(User)
admin.site.register(Plan)
admin.site.register(Task)
admin.site.register(Report)
