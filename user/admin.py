from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'date_joined',
    )

    fields = (
        'username',
        'password',
        'first_name',
        'last_name',
        'date_joined',
        'avatar',
    )

    list_display_links = ('username',)
