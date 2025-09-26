from django.contrib import admin

from .models import Department, Agent, DepartmentAgent

admin.site.register(Department)
admin.site.register(Agent)
admin.site.register(DepartmentAgent)
