from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .forms import *
from .models import *
# Register your models here.


class AuPairUserProfileAdmin(BaseUserAdmin):
    add_form = AuPairUserProfileForm
    model = AuPairProfile
    list_display = ('state', 'description')
    list_filter = ('user',)
    fieldsets = (
        (None, {'fields': ()}),
        ('Personal info', {'fields': ('date_of_birth', 'town', 'state', 'zipcode', 'description')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'town',
                'state',
                'zipcode',
                'description',
            )}
         ),
    )

    search_fields = ('town',)
    ordering = ('town',)
    filter_horizontal = ()


class AuPairUserAdmin(BaseUserAdmin):
    add_form = AuPairUserCreationForm
    form = AuPairUserChangeForm
    model = AuPairUser
    list_display = ('email', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'agency')}),
        ('Permissions', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
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
admin.site.register(AuPairProfile, AuPairUserProfileAdmin)
admin.site.unregister(Group)
