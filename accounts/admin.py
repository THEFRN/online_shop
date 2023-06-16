from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'username')

# admin.site.register(CustomUser, CustomUserAdmin)
