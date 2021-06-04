from django.contrib import admin

# Register your models here.
from .models import UserAccount
# Register your models here.


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'name', 'email', 'phone']
