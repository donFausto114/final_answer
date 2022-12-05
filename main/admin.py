from django.contrib import admin
from .models import Company, Investments

admin.site.register([Company, Investments])
