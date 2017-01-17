from django.contrib import admin

from .models import Wage, Title, Department, Government, Agency


admin.site.register(Wage)
admin.site.register(Title)
admin.site.register(Government)
admin.site.register(Agency)
admin.site.register(Department)
