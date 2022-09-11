from django.contrib import admin

from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'age', 'salary', 'qualification', 'designation', 'image')


admin.site.register(Employee, EmployeeAdmin)
