from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm  # Use the default UserCreationForm
    list_display = ('username', 'email', 'date_joined', 'last_login', 'is_staff', 'is_active')

# Register User with CustomUserAdmin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)S
