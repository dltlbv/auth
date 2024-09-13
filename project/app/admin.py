from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, EditProfileForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = UserRegistrationForm
    form = EditProfileForm
    model = CustomUser
    list_display = [
        "email",
        "username",
    ]


admin.site.register(CustomUser, CustomUserAdmin)
