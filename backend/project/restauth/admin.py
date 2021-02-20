from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .forms import *
from . models import *
# Register your models here.


class AuPairUserAdmin(BaseUserAdmin):
    add_form = AuPairUserCreationForm
    form = AuPairUserChangeForm
    model = AuPairUser
    list_display = ('email','admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email','password')}),
        ('Personal info', {'fields':('username','first_name','last_name','agency')}),
        ('Permissions', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':(
                'username',
                'email',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'agency',
                )}
        ),
    )

    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(AuPairUser, AuPairUserAdmin)
admin.site.unregister(Group)