from django.contrib import admin
from .models import CustomUserAuthentication
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserAuthentication

admin.site.register(CustomUserAuthentication, UserAdmin)