from django.contrib import admin

from .models import User, Vacancy, Employer

# Register your models here.
admin.site.register(User)
admin.site.register(Vacancy)
admin.site.register(Employer)