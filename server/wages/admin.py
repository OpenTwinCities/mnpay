from django.contrib import admin

from .models import Wage, Title, Department, Agency


admin.site.register(Wage)
admin.site.register(Title)
admin.site.register(Department)
admin.site.register(Agency)
