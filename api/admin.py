from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()
# Register your models here.
"""
admin.site.register(Account)
admin.site.register(Job)
admin.site.register(Offer)
admin.site.register(Review)
"""# users/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
#from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

admin.site.register(User, CustomUserAdmin)
#admin.site.register(User)
admin.site.register(Job)
admin.site.register(Offer)
admin.site.register(Review)
admin.site.register(Order)